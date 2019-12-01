import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

class compareImg :
    def __init__(self) :
        pass

    def readImg(self, filepath) :
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        return img

    def diffImg(self, img1, img2) :
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = bf.match(des1,des2)

        matches = sorted(matches, key = lambda x:x.distance)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        good = []
        for m,n in matches:
            if m.distance < 0.85 * n.distance:
                good.append([m])

        knn_image = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
#        plt.imshow(knn_image)
#        plt.show()

        if(len(good) >= 15) :
            global flag
            flag = True

    def run(self, user='') :
        filepath1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), (user+'.jpg'))
        filepath2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), ('logindata/'+user+'.jpg'))

        img1 = self.readImg(filepath1)
        img2 = self.readImg(filepath2)

        self.diffImg(img1, img2)
        if(flag) :
            print("Hi, %s!" % (user))
            with open("userdata/current.dat", "w") as cur :
                cur.write(user)
        else :
            print("You need to sign up first.")

flag = False
if __name__ == '__main__' :
    cImg = compareImg()
    cImg.run('SeungMin')
