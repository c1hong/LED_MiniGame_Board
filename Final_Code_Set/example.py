from pulse_sensor import Pulsesensor
import time

p = Pulsesensor()
p.startAsyncBPM()

def pulse() :
    try :
        while True:
            bpm = p.BPM
            if bpm > 120:
                print("Your BPM is too high. Please calm down. (Current : %d)" % bpm)
                time.sleep(2)
            else:
                return
            time.sleep(0.001)
    except:
        p.stopAsyncBPM()


