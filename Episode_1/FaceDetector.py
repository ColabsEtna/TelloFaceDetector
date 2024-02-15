import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
_, img = cap.read()

def find_face():
    facecascade = cv2.CascadeClassifier("./ressources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(imgGray, 1.2, 8)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)
        cx = x + w // 2
        cy = y + h // 2
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)



while True:
    _, img = cap.read()
    if img is not None:
        find_face(img)
        cv2.imshow("Output", img)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()