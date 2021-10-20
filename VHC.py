import cv2 as cv
import time as t
import numpy as np
import FPS as f
import HDM as h
import math as m

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

t = 0
wCam, hCam = 640, 480
cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = h.handDetect(detectionCon=0.8)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
# print(volume.GetVolumeRange())
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volbar = 400
volper = 0
while True:
    sucess, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:
        #print(lmlist[4], lmlist[8])
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        cv.circle(img, (x1, y1), 15, (245, 100, 255), cv.FILLED)
        cv.circle(img, (x2, y2), 15, (245, 100, 255), cv.FILLED)
        cv.line(img, (x1, y1), (x2, y2), (245, 100, 255), 2)
        cv.circle(img, (cx, cy), 15, (245, 100, 255), cv.FILLED)
        l = m.hypot(x2-x1, y2-y1)
        # print(l)
        # Hand Range 50 - 300
        # Vol Range -65 - 0
        vol = np.interp(l, [30, 300], [minVol, maxVol])
        volbar = np.interp(l, [50, 300], [400, 150])
        volper = np.interp(l, [50, 300], [0, 100])
        print(int(l), vol)
        volume.SetMasterVolumeLevel(vol, None)
        if l < 30:
            cv.circle(img, (cx, cy), 15, (0, 255, 0), cv.FILLED)
    cv.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv.rectangle(img, (50, int(volbar)), (85, 400), (255, 0, 0), cv.FILLED)
    F, t = f.fps(t)
    cv.putText(img, f'FPS: {int(F)}', (10, 80),
               cv.FONT_HERSHEY_COMPLEX, 1, (245, 100, 255), 3)
    cv.putText(img, f'Vol: {int(volper)}%', (40, 450),
               cv.FONT_HERSHEY_COMPLEX, 1, (245, 100, 255), 3)
    cv.imshow("Image", img)
    cv.waitKey(1)
