# Gestion Ventes

Application web de gestion de clients, développée en Python pur sans framework.
Elle repose sur une architecture **MVC** (Modèle - Vue - Contrôleur).

---

## Fonctionnalités

- Lister les clients
- Ajouter un client
- Modifier un client
- Supprimer un client

---

## Architecture MVC

```
app.py                   → Point d'entrée, serveur HTTP
routes.py                → Table de routage (URL → controller)
config.py                → Configuration (hôte, port, base de données)
database.py              → Connexion à la base de données MariaDB
controllers/
    client_controller.py → Logique de traitement des requêtes
models/
    client_model.py      → Accès aux données
sql/
    client_queries.py    → Requêtes SQL
views/
    client_view.py       → Génération du HTML
templates/
    client_list.html     → Liste des clients
    client_add.html      → Formulaire d'ajout
    client_edit.html     → Formulaire de modification
static/
    style.css            → Feuille de styles
    script.js            → Scripts JavaScript
```

---

## Prérequis

- Python 3.14+
- MariaDB

---

## Installation

**1. Cloner le projet**
```bash
git clone https://github.com/caucrogeGit/Gestion-Ventes.git
cd Gestion-Ventes
```

**2. Créer et activer l'environnement virtuel**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Installer les dépendances**
```bash
pip install -r requirements.txt
```

**4. Configurer les variables d'environnement**
```bash
cp .env.exemple .env
```

Renseigner les valeurs dans `.env` :
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=Ventes
DB_USER_LOGIN=votre_utilisateur
DB_USER_PWD=votre_mot_de_passe

APP_HOST=127.0.0.1
APP_PORT=8000
```

**5. Importer la base de données**

Les scripts SQL sont disponibles dans `Ressources/` selon votre SGBD :
```bash
mysql -u votre_utilisateur -p < Ressources/Ventes_mysql.sql
```

---

## Démarrage

```bash
python3 app.py
```

L'application est accessible sur : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Dépendances

| Package | Version | Rôle |
|---|---|---|
| `mariadb` | 1.1.14 | Connecteur MariaDB |
| `python-dotenv` | 1.2.2 | Chargement du fichier `.env` |
| `packaging` | 26.0 | Gestion des versions de paquets |
