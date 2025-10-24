# 🎮 Jeu du Casse-Brique (Tkinter + Python)

Un petit jeu du **casse-briques** développé en **Python** avec **Tkinter**.
Le but : faites rebondir la balle sur la plateforme pour détruire toutes les briques sans les laisser tomber !


#  Installation & exécution

# Étape 1 : Cloner le projet

Créez un dossier et clonez le dépôt :

git clone https://github.com/rakouzaine/Casse_Brique.git
cd Casse_Brique

# Étape 2 : Ouvrir le projet dans Visual Studio Code

code .


# Étape 3 : Créer un environnement virtuel

(Sous Windows)

python -m venv .venv
.venv\Scripts\activate


(Sous Linux / macOS )


python3 -m venv .venv
source .venv/bin/activate


# Étape 4 : Installer les dépendances

Toutes les dépendances sont listées dans le fichier `requirements.txt`.
Installe-les en une seule commande :

pip install -r requirements.txt



# Étape 5 : Lancer le jeu

Exécute simplement le fichier principal :

python CASSE_BRIQUE_COMPLET.py


ou selon ta configuration :


python3 CASSE_BRIQUE_COMPLET.py


## 🧠 Règles du jeu

1. Déplace la plateforme avec les flèches gauche et droite du clavier.
2. Fais rebondir la balle pour casser les briques.
3. Chaque brique détruite rapporte 10 points.
4. Tu disposes de 3 vies. Si la balle tombe en bas, tu perds une vie.
5. La partie se termine lorsque toutes les briques sont détruites ou que tu perds toutes tes vies.


# Sauvegarde du meilleur score

Le jeu enregistre automatiquement ton meilleur score dans :

meilleur_score.txt


# Amuse-toi bien !

> Si tu souhaites partager une version améliorée du jeu, n’hésite pas à faire un **fork** du dépôt et à proposer une **pull request** 💡

