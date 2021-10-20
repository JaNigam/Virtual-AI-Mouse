import cv2 as cv
import mediapipe as mp
import time as t
import HDM as h
import FPS as f
t = 0
#pTime = 0
#cTime = 0
cap = cv.VideoCapture(0)
detector = h.handDetect()
while True:
    sucess, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    if len(lmlist) != 0:
        print(lmlist[4])
#    cTime = t.time()
#    fps = 1/(cTime-pTime)
#    pTime = cTime
    F, t = f.fps(t)
    cv.putText(img, str(int(F)), (10, 70),
               cv.FONT_HERSHEY_COMPLEX, 3, (245, 100, 255), 3)
    cv.imshow("Image", img)
    cv.waitKey(1)
