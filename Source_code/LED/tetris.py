from matrix import *
import LED_display as TLD # added by cwhong on 20191129
import random
import threading
import keyboard
import time

class Key :

    def __init__(self) :
        self.key = ''
    
    def key_input(self, e) :
        for code in keyboard._pressed_events :
            if code == 17 :
                self.key = 'w'
            elif code == 31 :
                self.key = 's'
            elif code == 30 :
                self.key = 'a'
            elif code == 32 :
                self.key = 'd'
            elif code == 16 :
                self.key = 'q'
            elif code == 57 :
                self.key = ' '

def draw_matrix(m): # modified by cwhong on 20191129
    array = m.get_array()
    for y in range(m.get_dy()-4):
        for x in range(4,m.get_dx()-4):
            if array[y][x] == 0:
               # print("0", end='')
                TLD.set_pixel(y,19-x,0)
                continue
            elif array[y][x] == 1:
               # print("1", end='')
                TLD.set_pixel(y,19-x,4)
            else:
               # print("XX", end='')
                continue


###
### initialize variables
###     
I = [ [ [ 0 , 0 , 1 ,0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] ], # 일자
       [ [ 1 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] ],
       [ [ 1 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
L = [ [ [ 1 , 0 , 0 , 0 ] , [ 1 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ], #ㄴ자
       [ [ 1 , 1 , 0 , 0 ] , [ 1 , 0 , 0 , 0 ] , [ 1 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 1 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
H = [ [ [ 0 , 1 , 0 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ], #H 반쪽
       [ [ 0 , 0 , 1 , 1 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 0 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 1 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
T = [ [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ], #ㅗ 자
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 1 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
a = [ [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ], #H 반쪽 2
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]
b = [ [ [ 0 , 0 , 0 , 1 ] , [ 0 , 1 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ], #ㄴ 거울
       [ [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 0 ] , [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 1 ] , [ 0 , 1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 0 , 1 , 1 ] , [ 0 , 0 , 0 , 1 ] , [ 0 , 0 , 0 , 1 ] , [ 0 , 0 , 0 , 0 ] ] ]
c = [ [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ], # 2*2 정사각형
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ],
       [ [ 0 , 1 , 1 , 0 ] , [ 0 , 1 , 1 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ] ]

### integer variables: must always be integer!
iScreenDy = 32
iScreenDx = 16
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2
h=random.randint(0, 6)
i=0
arrayBlk=[I,L,H,T,a,b,c]
newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###

t=threading.Thread(target=TLD.main, args=())
t.setDaemon(True)
t.start()

iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk[h][i])
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen);

###
### execute the loop
###

K = Key()
while True:
    K.key = ''
    time.sleep(0.2)
    keyboard.hook(K.key_input)
    if K.key == 'q':
        print('Game terminated...')
        break
    elif K.key == 'a': # move left
        left -= 1
    elif K.key == 'd': # move right
        left += 1
    elif K.key == 's': # move down
        top += 1
    elif K.key == 'w': # rotate the block clockwise
        i=(i+1)%4
        currBlk=Matrix(arrayBlk[h][i])
    elif K.key == ' ': # drop the block
        while not tempBlk.anyGreaterThan(1):
            top+=1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
            if tempBlk.anyGreaterThan(1):
                top-=1
                newBlockNeeded = True

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if K.key == 'a': # undo: move right
            left += 1
        elif K.key == 'd': # undo: move left
            left -= 1
        elif K.key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif K.key == 'w': # undo: rotate the block counter-clockwise
            i = (i-1)%4
            currBlk = Matrix(arrayBlk[h][i])
        elif K.key == ' ': # undo: move up
            print('Not implemented')

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen);

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        h = random.randint(0,6)
        i = 0
        currBlk = Matrix(arrayBlk[h][i])
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen);
    
    top += 1
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        top-=1
        newBlockNeeded = True
###
### end of the loop
###
