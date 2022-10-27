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
chmod +x 3asri-projetintegration/setup.sh
./3asri-projetintegration/setup.sh
```

Et terminer l'installation en compilant l'espace de travail:
```bash
catkin build
. devel/setup.bash
```

-------------------------------

Si vous désirez apporter des modifications (alors faites sur une nouvelle branche), vous devrez exécuter le script:
```bash
cd hc10_moveit_config
chmod +x git_prepare.sh
./git_prepare.sh
```
avant de `git add`, `git commit` et `git push`.
