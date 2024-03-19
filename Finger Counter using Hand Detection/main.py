import numpy as np
import mediapipe as mp
import cv2
import HandTrackingModule as htm
import os
import time
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe.python.solutions.drawing_styles as drawing_styles

wCam, hCam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

folderPath = "Fingers"
myList = os.listdir(folderPath)
# print((myList))
myList = sorted(myList)
old_overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    old_overlayList.append(image)

# sorted_list = sorted(old_overlayList)
# print(sorted_list)
pTime = 0
detector = htm.handDetector(detectionCon=1)   

tipIds = [4,8,12,16,20]

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) !=0:
        fingers = []

        ## For thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        ##For 4 fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)
        print(totalFingers)

        h,w,c = old_overlayList[0].shape
        img[0:h,0:w] = old_overlayList[totalFingers -1]


        cv2.rectangle(img, (0,100), (100,200), (0,255,0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (25,175), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, f'FPS:{int(fps)}',(250,50),cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 3)



    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()















