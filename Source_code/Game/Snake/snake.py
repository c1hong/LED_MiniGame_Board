import keyboard as kbd
import random as rd
import time
import os

# ===== Exception ===== #

class EscInput(Exception) :                         # 종료 입력
    def __init__(self) :
        pass

class MapOverAccess(Exception) :                    # 구역 지정
    def __init__(self) :
        pass
        
# ===================== #

class Snake :
    
    LIST = ['●', '▲', '▼', '◀', '▶']            # 출력할 문자
    WAY = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)] # 움직이는 방향
    
    def __init__(self):
        self.pos = [(8, 13)]                         # 기본 위치
        self.dir = 4                                 # 1-North, 2-South, 3-West, 4-East

    def add_body(self) :
        x, y = self.pos[-1]
        head = self.dir
        W_x, W_y = self.WAY[head]
        if not 0 < x+W_x < 15 or not 0 < y+W_y < 26 : # 맵 초과 접근 에러
            raise MapOverAccess
        self.pos.append((x+W_x, y+W_y))              # 몸통은 유지, 머리를 갱신
        self.bodypart = self.pos.pop(0)

    def change_head(self, e) :                      # 머리 방향
        for code in kbd._pressed_events :
            if code == 17 or code == 72 :
                self.dir = 1
            elif code == 31 or code == 80 :
                self.dir = 2
            elif code == 30 or code == 75 :
                self.dir = 3
            elif code == 32 or code == 77 :
                self.dir = 4
            elif code == 1 :
                self.dir = -1

class Food :
    def __init__(self) :
        self.pos = (rd.randint(1, 14), rd.randint(1, 25))

    def set_food(self, rd_pos) :
        self.pos = rd_pos

    def chk_food(self, A, B) :
        return A == B
    
class Map :
    N = 16
    M = 27
    def __init__(self, player) :
        self.snake = player
        self.food = Food()

    def place_food(self) :                          # 랜덤 생성
        x, y = rd.randint(1, 14), rd.randint(1, 25)
        for n in self.snake.pos :
            if n == (x, y) :
                self.place_food()
        self.food.set_food((x, y))

    def print_map(self) :                           # 테스트 전용 출력 방식
        for i in range(self.N) :
            for j in range(self.M) :
                if i % 15 == 0 or j % 26 == 0 :
                    print('■', end='')
                elif (i, j) == self.snake.pos[-1] :
                    print(self.snake.LIST[self.snake.dir], end='')
                    if(self.food.chk_food((i, j), self.food.pos)) :
                        self.snake.pos.insert(0, self.snake.bodypart)
                        self.place_food()
                elif (i, j) in self.snake.pos :
                    print('●', end='')
                elif (i, j) == self.food.pos :
                    print('★', end='')
                else :
                    print('□', end='')
            print()

# __main__ #

if __name__ == '__main__' :

    S = Snake()
    M = Map(S)

    try :
        while True :
            S.add_body()
            kbd.hook(S.change_head)
            if S.dir == -1 :
                raise EscInput
            M.print_map()
            time.sleep(0.05)
            os.system('cls' if os.name == 'nt' else 'clear')
    except MapOverAccess :
        print('맵을 벗어났습니다.')
    except EscInput :
        print('ESC가 입력되어 게임을 종료합니다.')
