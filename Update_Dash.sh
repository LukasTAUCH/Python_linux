# Ce dossier permet d'actualiser notre dashboard avec les nouvelles data de notre csv
# Le problème etant que des processus tourne en arrière plan
# Si nous avions fait un crontab -e puis /usr/bin/python3 /path/Interface_Dashboard.py 
# Donc il y a création de processus dans notre système
# Pour les voir ps -ax 
# pour kill sudo kill -9 [lenombre_key du processus]

# Donc ici on automatise en killant tous les processus ayant pour port le 8050 qui est notre serveur dashboard
# Puis on relance notre serveur
sudo fuser -k 8050/tcp
/usr/bin/python3 /home/ec2-user/Projet_Linux_Python/Interface_Dashboard.py
