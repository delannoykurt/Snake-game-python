# 🐍 Snake Game – Projet Python

Un jeu Snake codé en Python à l’aide de la bibliothèque `pygame`. Ce projet a été conçu comme un **exercice complet d’apprentissage** du langage Python, incluant la gestion d’une boucle de jeu, d’une interface graphique, et d’une architecture modulaire propre.

---

## 🎯 Objectifs pédagogiques

- Maîtriser les **bases de `pygame`**
- Comprendre la **boucle de jeu**
- Gérer les **événements clavier**, les **collisions**, le **score**
- Structurer un projet Python comme un pro
- Devenir **autonome en Python**

---

## 📸 Aperçu

> *(Ajoutez une capture d’écran du jeu ici une fois fonctionnel)*

---

## 📁 Structure du projet
snake-game/
├── main.py               # point d’entrée du jeu
├── game/
│   ├── __init__.py
│   ├── snake.py          # logique du serpent
│   ├── food.py           # logique de la nourriture
│   ├── game_engine.py    # logique principale (collision, score, etc.)
├── assets/
│   ├── (optionnel: images, sons)
├── README.md


---

## 🚀 Lancer le jeu

### Prérequis

- Python 3.7+
- pygame


### 💡 Option recommandée : Utiliser un environnement virtuel

Pour isoler les dépendances du projet :

```bash
# Créer un environnement virtuel
python -m venv venv

# L’activer
# Sous Windows :
venv\Scripts\activate
# Sous macOS/Linux :
source venv/bin/activate

# Installer les dépendances
pip install pygame

# Geler les dépendances dans un fichier requirements.txt
pip freeze > requirements.txt

### Lancement
python main.py
