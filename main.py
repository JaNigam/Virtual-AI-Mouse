import cv2 as cv
import mediapipe as mp
import time as t

mpHands = mp.solutions.hands
#to draw the hand
mpDraw = mp.solutions.drawing_utils
#initializes a mediapipe hand object
#by default number of hands detected = 2 we can change it to one if needed
hands = mpHands.Hands(max_num_hands = 1)

#for checking the fps
prevTime = 0
currTime = 0


# VideoCapture(0) connects to default webcam connected
cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#throughout this program landmark refers to the points shown on the hand
while True:
    success, img = cap.read()
    # hands object uses only RGB image hence we need to convert the BGR(by default in openCV) image to RGB
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    #print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            for land_mark_id, land_mark in enumerate(hand.landmark):
                # print(land_mark_id, land_mark)
                # #converting the x y position of points/landmarks to pixel format
                img_h, img_w, img_c = img.shape
                pos_x, pos_y = int(land_mark.x * img_w), int(land_mark.y * img_h)
                #for index finger tip the id is 8
                if land_mark_id == 8:
                    cv.circle(img, (pos_x, pos_y), 20, (0, 255, 0), cv.FILLED)
            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)

    #fps caluculation
    currTime = t.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime

    #showing fps in the window
    cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)

    cv.imshow('video', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
