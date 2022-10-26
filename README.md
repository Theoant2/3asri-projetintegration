# Procédure d'installation


Dans un répertoire, créer votre espace de travail et ajouter ROS:
```bash
mkdir -p catkin_ws/src
cd catkin_ws
. /opt/ros/noetic/setup.bash    
```

Télécharger ensuite le dépôt contenant le modèle du robot Yaskawa HC10:
```bash
cd src
git clone https://github.com/ros-industrial/motoman.git
```

Et celui contenant notre travail (branche `master`):
```bash
cd src
git clone https://github.com/Theoant2/3asri-projetintegration.git
```

Exécuter le script d'initialisation:
```bash
chmod +x setup.sh
./setup.sh
```

Et terminer l'installation en compilant l'espace de travail:
```bash
catkin build
. devel/setup.bash
```
