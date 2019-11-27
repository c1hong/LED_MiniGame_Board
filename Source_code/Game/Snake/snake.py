import keyboard as kbd
import random as rd
import threading
import time
import os

# ===== Exception ===== #

class EscInput(Exception) :                         # 
    def __init__(self) :
        pass

class MapOverAccess(Exception) :                    #
    def __init__(self) :
        pass

class BodyTouch(Exception) :
    def __init__(self) :
        pass
        
# ===================== #

class Snake :
    
    LIST = ['t', 'r', 'e', 'w', 'q']            # 
    WAY = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)] # 
    
    def __init__(self):
        self.pos = [(8, 13)]                         # 
        self.dir = 4                                 # 1-North, 2-South, 3-West, 4-East

    def add_body(self) :
        x, y = self.pos[-1]
        head = self.dir
        W_x, W_y = self.WAY[head]
        if not 0 < x+W_x < 15 or not 0 < y+W_y < 26 : # 
            raise MapOverAccess
        elif (x+W_x, y+W_y) in self.pos :
            raise BodyTouch
        self.pos.append((x+W_x, y+W_y))              # 
        self.bodypart = self.pos.pop(0)

    def change_head(self, e) :                      # 
        for code in kbd._pressed_events :
            if (code == 17 or code == 72) and self.dir != 2:
                self.dir = 1
            elif (code == 31 or code == 80) and self.dir != 1:
                self.dir = 2
            elif (code == 30 or code == 75) and self.dir != 4:
                self.dir = 3
            elif (code == 32 or code == 77) and self.dir != 3:
                self.dir = 4
            elif code == 1 :
                self.dir = -1

class Food() :
    def __init__(self) :
        self.pos = []

    def thread_food(self) :                             #
        while True :
            (x, y) = ((rd.randint(1, 14), rd.randint(1, 25)))
            if not self.chk_food((x, y)) :
                self.set_food((x, y))
            time.sleep(10)

    def set_food(self, rd_pos) :
        self.pos.append(rd_pos)

    def remove_food(self, rm_pos) :
        self.pos.remove(rm_pos)

    def chk_food(self, chk_pos) :
        return chk_pos in self.pos
    
class Map :
    N = 16
    M = 27
    def __init__(self, player) :
        self.snake = player
        self.food = Food()

    def place_food(self) :                          # 
        x, y = rd.randint(1, 14), rd.randint(1, 25)
        for n in self.snake.pos :
            if n == (x, y) :
                self.place_food()
        self.food.set_food((x, y))

    def print_map(self) :                           # --  -- #
        for i in range(self.N) :
            for j in range(self.M) :
                if i % 15 == 0 or j % 26 == 0 :
                    print('a', end='')
                elif (i, j) == self.snake.pos[-1] :
                    print(self.snake.LIST[self.snake.dir], end='')
                    if self.food.chk_food((i, j)) :
                        self.snake.pos.insert(0, self.snake.bodypart)
                        self.place_food()
                        self.food.remove_food((i, j))
                elif (i, j) in self.snake.pos :
                    print('b', end='')
                elif (i, j) in self.food.pos :
                    print('c', end='')
                else :
                    print('d', end='')
            print()

# __main__ #

if __name__ == '__main__' :
    
    S = Snake()
    M = Map(S)
    t = threading.Thread(target=M.food.thread_food, args=())    #
    t.setDaemon(True)                                           # 
    t.start()

    try :
        while True :
            S.add_body()
            kbd.hook(S.change_head)
            if S.dir == -1 :
                raise EscInput
            M.print_map()
            time.sleep(0.1)
            os.system('cls' if os.name == 'nt' else 'clear')
    except MapOverAccess :                                      # --- #
    except BodyTouch :
    except EscInput :
