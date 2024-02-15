
# TelloFaceTracker

Vous voici dans l'épisode1 des ateliers Colabs, le but de ce projet est de programmer un drone pour qu'il puisse nous suivre en fonction de notre visage.


----

**Table of Contents**

- [Installation et Lancement](#installation-et-lancement)
  * [Installation](#installation)
  * [Lancement](#lancement)
    + [Lancement de la detection du visage](#lancement-de-la-detection-du-visage)
    + [Lancement du drône](#lancement-du-dr-ne)
    + [Lancement de la detection du visage avec le drône](#lancement-de-la-detection-du-visage-avec-le-dr-ne)
- [Links](#links)
- [Fonction utilisées](#fonction-utilis-es)
  * [Fonction utilisées de Tello](#fonction-utilis-es-de-tello)
  * [Fonction utilisées de OpenCV](#fonction-utilis-es-de-opencv)
    + [Fonction de modification vidéo](#fonction-de-modification-vid-o)
    + [Fonction IA de OpenCv](#fonction-ia-de-opencv)
- [FlowChart](#flowchart)

----

# Installation et Lancement

## Installation 

```bash
  pip install djitellopy
  pip install opencv-python
```


## Lancement 

### Lancement de la detection du visage

```bash
  python3 FaceDeteactor.py ## pour Lancer le FaceTracker sans le drone
```

### Lancement du drône

```bash
  python3 TelloBase.py ## pour Lancer le drone
```

### Lancement de la detection du visage avec le drône

```bash
  python3 TelloFaceTracker.py ## pour Lancer le FaceTracker avec le drone
```



# Links

[OpenCV documentation](https://docs.opencv.org/3.4/annotated.html)

[Tello drône documentation](https://djitellopy.readthedocs.io/en/latest/tello/#djitellopy.Tello)



# Fonction utilisées

## Fonction utilisées de Tello

Fonction name | Decription | Paramètres
------------- | ------------- | -------------
`tello.Tello()` | Init la connexion au drône | aucuns utilisés
`connect()`   | Etablie connecte au drône | aucuns utilisés
`streamon()`   | Allume la caméra du drône | aucuns utilisés
`takeoff()`   | Fait décoler le dône | aucuns utilisés
`send_rc_control()`   | Déplace le drône | left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
`get_frame_read().frame`   | Récupere le flux vidéo | aucuns utilisés
`land()`   | Fait attérir le drône | aucuns utilisés
`get_battery()`   | Récupère la batterie | aucuns utilisés


## Fonction utilisées de OpenCV

### Fonction de modification vidéo

Fonction name | Decription 
------------- | -------------
`VideoCapture(0)` | Précise l'entré vidéo
`read()`   | récupère la vidéo 
`imshow()`   | Affiche la vidéo
`waitKey()`   | Attend une touche  
`destroyAllWindows()`   | Supprime la fenêtre de imshow 
`cvtColor()`   | Change la couleur de la vidéo 
`rectangle()`   | Créer un rectangle sur la vidéo 
`circle()`   | Créer un cercle sur la vidéo 

### Fonction IA de OpenCv


[OpenCV documentation detection d'objets](https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498)


Fonction name | Decription | Paramètres
------------- | ------------- | -------------
`CascadeClassifier()`   | Initialise le classifier d'objet ou de visage | Nom du fichier à partir duquel le classificateur est chargé.
`detectMultiScale()`   | Détecte les objets de différentes tailles dans l'image d'entrée | aucuns utilisés

# FlowChart

```flow
st=>start: Drône
op=>operation: Vidéo
cond=>condition: Vidéo reçu Oui ou Non?
e=>end: PC detection faciale

st->op->cond
cond(yes)->e
cond(no)->op
```

