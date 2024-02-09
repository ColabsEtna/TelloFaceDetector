from djitellopy import tello
import cv2
import numpy as np
import time

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()
me.takeoff()
me.send_rc_control(0,0,25,0)

time.sleep(2.2)

fbrange = [6200, 6800]
pid = [0.4, 0.4, 0]
perror = 0

w, h = 360, 240

def find_face(img):
    facecascade = cv2.CascadeClassifier("./ressources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(imgGray, 1.2, 8)

    myfacelist = []
    myfaceListArea = []

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h

        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

        myfacelist.append([cx, cy])
        myfaceListArea.append(area)
    if len(myfaceListArea) != 0:
        i = myfaceListArea.index(max(myfaceListArea))
        return img, [myfacelist[i], myfaceListArea[i]]
    else :
        return img, [[0,0], 0]

    

def track_face(info, w, pid, perror):
    area = info[1]
    x,y = info[0]
    error = x - w //2
    speed = pid[0] * error + pid[1] * (error - perror)
    speed = int(np.clip(speed, -100, 100))
    fb = 0


    if area > fbrange[0] and area < fbrange[1]:
        fb = 0
    elif area > fbrange[1]:
        fb =-20
    elif area < fbrange[0] and area != 0:
        fb = 20

    print(error, fb)

    if x == 0:
        speed = 0
        error = 0
    me.send_rc_control(0, fb, 0, speed)
    return error


while True:
    img = me.get_frame_read().frame
    if img is not None:
        img = cv2.resize(img, (360, 240))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img, info = find_face(img)
        perror = track_face(info, w, pid, perror)
        cv2.imshow("Output", img)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break


cv2.destroyAllWindows()