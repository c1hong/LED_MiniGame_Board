import SIFT_face 
from urllib.request import urlopen, urlretrieve#, request
import os
import webbrowser

USER_NAME = input("User Name? : ")
#os.system('raspistill -o '+USER_NAME+'.jpg')
try :
    img = SIFT_face.compareImg()
    img.run(USER_NAME)
except :
    pass

