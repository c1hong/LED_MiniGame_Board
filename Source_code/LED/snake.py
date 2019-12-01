from FINAL_display import end
import LED_display as LD
import keyboard as kbd
import random as rd
import threading
import time
import os

# ========== Snake ========== #

class Snake :
    
    N = 32
    M = 16
    LIST = ['t', 'r', 'e', 'w', 'q']
    WAY = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def __init__(self):
        self.pos = [(1, 1)]
        self.dir = 4

    def add_body(self) :
        x, y = self.pos[-1]
        head = self.dir
        W_x, W_y = self.WAY[head]
        if not 0 <= x+W_x <= self.N-1 or not 0 <= y+W_y <= self.M-1 :
            raise Exception
        elif (x+W_x, y+W_y) in self.pos :
            raise Exception
        self.pos.append((x+W_x, y+W_y))
        self.bodypart = self.pos.pop(0)

    def change_head(self, e) :
        for code in kbd._pressed_events :
            if (code == 17 or code == 72) and self.dir != 2:
                self.dir = 1
            elif (code == 31 or code == 80) and self.dir != 1:
                self.dir = 2
            elif (code == 30 or code == 75) and self.dir != 3:
                self.dir = 4
            elif (code == 32 or code == 77) and self.dir != 4:
                self.dir = 3

class Food() :
    def __init__(self) :
        self.pos = []

#   def thread_food(self) :
#       while True :
#           (x, y) = ((rd.randint(0, 31), rd.randint(0, 15)))
#           if not self.chk_food((x, y)) :
#               self.set_food((x, y))
#           time.sleep(10)

    def set_food(self, rd_pos) :
        self.pos.append(rd_pos)

    def remove_food(self, rm_pos) :
        self.pos.remove(rm_pos)

    def chk_food(self, chk_pos) :
        return chk_pos in self.pos
    
class Map :

    def __init__(self, player) :
        self.snake = player
        self.food = Food()

    def place_food(self) :                           
        x, y = rd.randrange(1, 31), rd.randrange(1, 15)
        for n in self.snake.pos :
            if n == (x, y) :
                self.place_food()
        self.food.set_food((x, y))

    def fill_map(self) :                           
        for i in range(self.snake.N) :
            for j in range(self.snake.M) :
                color = -1
               #if i % (self.snake.N-1) == 0 or j % (self.snake.M-1) == 0 :
               #    color = 0
                if (i, j) == self.snake.pos[-1] :
                    color = 1
                    if self.food.chk_food((i, j)) :
                        score += 5000
                        self.snake.pos.insert(0, self.snake.bodypart)
                        if(len(self.snake.pos)%5==0) :
                            self.place_food()
                        self.food.remove_food((i, j))
                        self.place_food()
                elif (i, j) in self.snake.pos :
                    color = 3
                elif (i, j) in self.food.pos :
                    color = 4
                else :
                    color = 0

                LD.set_pixel(i, j, color)

# ========== __main__ ========== #

if __name__ == '__main__' :
    
    user = 'SeungMin'
    S = Snake()
    M = Map(S)
    M.place_food()
#   t = threading.Thread(target=M.food.thread_food, args=())
#   t.setDaemon(True)
#   t.start()

    score = 0
    t=threading.Thread(target=LD.main, args=())
    t.setDaemon(True)
    t.start()
    
    try :
        while True :
            S.add_body()
            kbd.hook(S.change_head)
            M.fill_map()
            score += 100
            time.sleep(0.1)
            os.system('cls' if os.name == 'nt' else 'clear')
    except :
        os.system('cls' if os.name == 'nt' else 'clear')
        filename = os.path.basename(__file__).replace('.py', '')
        end(filename, user, score) 
