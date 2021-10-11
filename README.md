# Projet_P4

Cette application permet de créer un tournoi d'échecs.      
Les données sont stockés dans une base de données TinyDB


# Pré-requis 
Création d'un environnement virtuel env  
python -m venv env  
activation de l'environnement virtuel : source env/bin/activate  
installation des packages : voir le fichier requirements.txt    

# Lancement du projet

Le programme est écrit en Python, copier tous les fichiers et repertoires du repository, et lancer le programme depuis un terminal via la commande :

python3 main_app.py

# Contenu du projet
1. Saisie des joueurs  
2. Créér un tournoi : le premier round est généré automatiquement   
3. Visualiser le round en cours
4. Saisir les scores
5. Mise à jour du classement des joueurs
6. Générer les rounds suivant

# Autres options du menu
* Rapports
* Mise à blanc des tables

# Output file 
db.json

# Tables
* players  
* tournament  
* round_match
* round
* score  

# Rapport flake8
Le dépôt contient un rapport flake ne contenant aucune erreur. Il est possible d'en générer un nouveau en installant le module flake8 et en saisissant dans le terminal (setup.cfg : fichier de configuration de flake8) :

flake8