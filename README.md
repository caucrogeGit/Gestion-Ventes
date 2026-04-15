# Squelette-projet-Python

Projet Python configuré avec :

- `pyenv` pour imposer la version de Python
- `venv` pour isoler les dépendances du projet
- `VS Code` comme éditeur
- `mariadb` comme connecteur Python vers MariaDB

---

## Objectif

Ce projet est conçu pour être utilisé avec une version précise de Python, sans modifier le Python système de Linux.

Ici, le projet utilise :

- **Python 3.14.4**
- un environnement virtuel local nommé **`.venv`**

Le but est d’avoir un projet :

- propre ;
- reproductible ;
- isolé ;
- compatible avec Git et GitHub.

---

## Contenu important du projet

Le projet contient notamment :

- `.python-version` : indique la version de Python attendue par `pyenv`
- `.gitignore` : ignore les fichiers et dossiers à ne pas envoyer sur Git
- `.venv/` : environnement virtuel local du projet
- `requirements.txt` : liste des dépendances Python installées

---

## Ce qui est versionné dans Git

On peut envoyer sur GitHub :

- le code source ;
- `.gitignore` ;
- `.python-version` ;
- `requirements.txt` ;
- `README.md`

---

## Ce qui n’est pas versionné

On n’envoie pas sur GitHub :

- `.venv/`
- `__pycache__/`
- `*.pyc`
- `.vscode/` sauf besoin particulier

Exemple de `.gitignore` utilisé :

```gitignore
.venv/
__pycache__/
*.pyc
.vscode/

## Configurer VS Code

Ouvrir le dossier du projet dans VS Code.

Ensuite :

1. `Ctrl + Shift + P`
2. taper `Python: Select Interpreter`
3. choisir l’interpréteur : .venv/bin/python
