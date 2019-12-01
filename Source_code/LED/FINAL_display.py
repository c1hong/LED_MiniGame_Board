import LED_display as LD
from datetime import datetime
import os

def snake(user, score) :
    now = datetime.now()
    link = os.path.join(os.path.dirname(os.path.abspath(__file__)), (user+'.dat'))
    with open(link, 'a') as f :
        log = str(now) + '\n' + user + '\'s Snake Game Score : ' + score + '\n\n'
        f.write(log)
    pass

def tetris(user, score) :
    now = datetime.now()
    link = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    with open(link, 'a') as f :
        log = str(now) + '\n' + user + '\'s Tetris Game Score : ' + score + '\n\n'
        f.write(log)
    pass

def end(__name, __user, __score) :
    try :
        eval('%s(__user, str(__score))' % (__name))
    except NameError :
        pass
