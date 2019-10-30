import keyboard as kbd
import random as rd
import time

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
        self.pos.append((x+W_x, y+W_y))              # 몸통은 유지, 머리를 갱신
        print(self.pos)

class Food :
    def __init__(self, pos) :
        self.pos = pos

    def printFood(self) :
        print(self.pos)
        
class Map :
    N = 16
    M = 27
    def __init__(self) :
        self.snake = Snake()

    def place_food(self) :
        x, y = rd.randint(1, 14), rd.randint(1, 25) # 랜덤한 위치
        for n in self.snake.pos :
            if n == (x, y) :
                self.place_food()
        self.food = Food((x, y))
        self.food.printFood()

def pressed_keys(e) : # 키보드 입력처리
    global key
    key = []
    for code in kbd._pressed_events :
        key.append(code)
        print(key)

key = list()
kbd.hook(pressed_keys)

S = Snake()
M = Map()
for i in range(3) : # 반복문 실행 중 hook가 동작하는지 테스트
    S.add_body()
    M.place_food()
    print()
    time.sleep(1.5) # 테스트를 위한 1.5초 딜레이
