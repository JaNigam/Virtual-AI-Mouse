import cv2 as cv
import mediapipe as mp
import time as t
import pyautogui as pag
import numpy as np
import math
import FPS as f


class handDetect():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.detectionCon, self.trackCon)

    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 10, (245, 100, 255), cv.FILLED)
        return lmlist


def main():
    #    pTime = 0
    #    cTime = 0
    t = 0
    cap = cv.VideoCapture(0)
    detector = handDetect()
    while True:
        sucess, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
            print(lmlist[4])
#        cTime = t.time()
#        fps = 1/(cTime-pTime)
#        pTime = cTime
#        cv.putText(img, str(int(fps)), (10, 70),
#                   cv.FONT_HERSHEY_COMPLEX, 3, (245, 100, 255), 3)
        F, t = f.fps(t)
        cv.putText(img, str(int(F)), (10, 70),
                   cv.FONT_HERSHEY_COMPLEX, 3, (245, 100, 255), 3)
        cv.imshow("Image", img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()
