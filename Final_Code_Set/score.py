import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'userdata/current.dat'), "r") as CUR :
    user = CUR.readlines()
    os.system('cat /home/pi/Downloads/'+user[0]+'.dat')
