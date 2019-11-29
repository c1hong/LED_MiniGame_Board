import keyboard as kbd

def func(e) :
    for code in kbd._pressed_events :
        print(code)

while(True) :
    kbd.hook(func)
    kbd.wait()
