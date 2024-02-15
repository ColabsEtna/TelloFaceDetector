from djitellopy import tello ## Librairie pour le dône Tello
import cv2 ## Librairie pour gestion des flux vidéo et IA

me = tello.Tello() ## Init connection au drône
me.connect() ## ce connecte au drône
print(me.get_battery()) ## Affiche la battery du drône

me.streamon() ## Allume la caméra du drône
me.takeoff() ## Fait décoler le drône
me.send_rc_control(0,0,25,0) ## Send_rc_control permet de déplacer le drône

while True:
    img = me.get_frame_read().frame ## Permet de récuperer le flux vidéo de la caméra du drône
    if img is not None: ## Check si l'image à bien était reçu
        img = cv2.resize(img, (360, 240)) ## Utilisation de OpenCV pour resize l'image
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) ## Utilisation de OpenCV pour changer la couleur de l'image
        cv2.imshow("Output", img) ## Utilisation de OpenCV pour afficher le flux vidéo du drône
    

    if cv2.waitKey(1) & 0xFF == ord('q'): ## Permet d'attendre une touche pour quitter => 0xFF == ord('q') attend la touche 'Q'
        me.land() ## Fait attérir le drône
        break
cv2.destroyAllWindows() ## Detruit la fenêtre de la vidéo