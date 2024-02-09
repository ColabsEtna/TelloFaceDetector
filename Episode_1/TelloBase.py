from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()
me.takeoff()
me.send_rc_control(0,0,25,0)

while True:
    img = me.get_frame_read().frame
    if img is not None:
        img = cv2.resize(img, (360, 240))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imshow("Output", img)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break
cv2.destroyAllWindows()