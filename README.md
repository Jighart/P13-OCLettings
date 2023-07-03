---
## Accès rapide
#### 1. [Objectifs](#objectifs)
#### 2. [Développement local](#dev)
#### 3. [Déploiement](#deploiement)

---

<a name="objectifs"></a>
# Objectifs 
**Projet 13 Python : Mettre à l'échelle une application Django en utilisant une architecture modulaire**

_Testé sous Windows 10 - Python 3.10.2 - Django 3.0_

Plusieurs domaines du site **OC Lettings** ont été améliorés à partir du projet
[Python-OC-Lettings-FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR) :

1) Réduction de la dette technique

   - Corriger les erreurs de linting
   - Corriger la pluralisation des noms de modèles dans le site d'administration


2) Refonte de l'architecture modulaire

   - Créer 3 applications *lettings*, *profiles* et *home* pour séparer les fonctionnalités de l'application
   - Convertir *oc_lettings_site* en projet Django
   - Développer une suite de tests


3) Ajout d'un pipeline CI/CD avec [CircleCI](https://circleci.com) et déploiement sur Azure

   1) *Compilation* : exécuter le linting et la suite de tests (sur toutes les branches)
   2) *Conteneurisation* : construire et push une image du site avec [Docker](https://www.docker.com) (si étape 1 réussie, branche *main* uniquement)
   3) *Déploiement* : mettre en service le site avec Azure (si étape 2 réussie, branche *main* uniquement)


4) Surveillance de l'application et suivi des erreurs via [Sentry](https://sentry.io/welcome/)


<a name="dev"></a>
# Développement local

## Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.7 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell 
exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

## Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Jighart/P13-OCLettings.git`

## Créer l'environnement virtuel

- `cd /path/to/P13-OCLettings`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement virtuel `source venv/bin/activate` (MacOS et Linux) ou `venv\Scripts\activate` (Windows)
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python` (MacOS et Linux) ou `(Get-Command python).Path` (Windows)
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip` (MacOS et Linux) ou `(Get-Command pip).Path` (Windows)
- Pour désactiver l'environnement, `deactivate`

<a name="env"></a>
## Variables d'environnement : fichier *.env*

Le fichier *.env* est généré automatiquement lors de la création de l'image Docker.

Pour une utilisation locale, le fichier *.env* est à créer manuellement selon ce modèle :

```
DJANGO_SECRET_KEY=<Your Django Key>
SENTRY_DSN=<Your Sentry DSN>
HOST_NAME=<URL of host repository to add in ALLOWED_HOST>
```


## Exécuter le site

- `cd /path/to/P13-OCLettings`
- `source venv/bin/activate` (MacOS et Linux) ou `venv\Scripts\activate` (Windows)
- `pip install -r requirements.txt`
- Lancer le serveur `python manage.py runserver`
- Aller sur http://127.0.0.1:8000/ dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

## Linting

- `cd /path/to/P13-OCLettings`
- `source venv/bin/activate` (MacOS et Linux) ou `venv\Scripts\activate` (Windows)
- `flake8`

## Tests unitaires

- `cd /path/to/P13-OCLettings`
- `source venv/bin/activate` (MacOS et Linux) ou `venv\Scripts\activate` (Windows)
- `pytest`

## Base de données

- `cd /path/to/P13-OCLettings`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

## Site d'administration

- Aller sur http://127.0.0.1:8000/admin/
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

## Docker

### Lancement de l'application en local via l'utilisation d'une image sur DockerHub
- Télécharger et installer [Docker](https://docs.docker.com/get-docker/)
- Aller sur le repository Docker : https://hub.docker.com/r/jighart/p13-oclettings/tags
- Copier le tag de l'image de votre choix (de préférence le plus récent)
- Utiliser la commande `docker run -p 8000:8000 jighart/p13-oclettings:<image-tag>`, en remplaçant *image-tag* par le tag de l'image souhaitée

Vous pouvez accéder à l'application dans un navigateur via http://127.0.0.1:8000/


<a name="deploiement"></a>
# Déploiement

## Prérequis
Afin d'effectuer le déploiement et l'intégration continue de l'application, les comptes suivants sont nécessaires :

- compte [GitHub](https://github.com/)
- compte [CircleCI](https://circleci.com) (connecté au compte GitHub)
- compte [Docker](https://www.docker.com)
- compte [Azure](https://portal.azure.com/)
- compte [Sentry](https://sentry.io/welcome/)


## Description
Le déploiement de l'application est automatisé par un pipeline CircleCI. 
Lorsque l'on push des modifications sur le repository GitHub, le pipeline déclenche l'exécution des tests et du linting du code. 
Ces opérations sont effectuées sur **toutes les branches du projet**.

Si des modifications sont apportées à la **branche main**, et si les tests et le linting sont réussis,
les opérations suivantes sont déclenchées :
- Création d'une image Docker et dépôt sur DockerHub
- Si l'étape précédente est réussie, déploiement de l'application sur Heroku


## Configuration

### CircleCI

Après avoir récupéré le projet, mis en place l'environnement de développement local (voir [Développement local](#dev))
et créé les comptes requis, initialiser un projet sur CircleCI via *"Set Up Project"*. 
Sélectionner la branche *main* comme source pour le fichier *.circleci/config.yml*.


Pour faire fonctionner le pipeline CircleCI, il est nécessaire de préciser des variables d'environnement (*Project Settings* > *Environment Variables*) :

| Variable CircleCI | Description                                                                             |
|-------------------|-----------------------------------------------------------------------------------------|
| SENTRY_DSN        | URL pour le projet Sentry (voir [Sentry](#sentry))                                      |
| DOCKER_LOGIN      | Nom d'utilisateur du compte Docker                                                      |
| DOCKER_PASSWORD   | Mot de passe du compte Docker                                                           |
| DOCKER_REPO       | Nom du repository sur DockerHub                                                         |
| HOST_URL          | Nom du site sur Azure. L'application déployée sera accessible via `https://<HOST_URL>/` |
| AZURE_USERNAME    | Nom de l'application web Azure                                                          |
| AZURE_PASSWORD    | Mot de passe du compte Azure                                                            |
| AZURE_REPO_URL    | URL du Container Registry sur Azure                                                     |


### Docker

Créer un repository sur DockerHub. Le nom du repository doit correspondre à la variable *DOCKER_REPO* définie pour CircleCI.

Le workflow de CircleCI va créer et déposer l'image de l'application dans le repository DockerHub défini, avec le tag **latest**.

### Azure

L'application web Azure est configurée pour automatiquement lancer le container nommé **p13-oclettings** et prendra le dernier envoyé sur
le container registry. Compter environ 3 minutes pour que le déploiement et le redémarrage s'effectue.


<a name="sentry"></a>
### Sentry

Après avoir créé un compte [Sentry](https://sentry.io/welcome/), créer un projet pour la plateforme Django. Le SENTRY_DSN sera disponible
dans *Project Settings > Client Keys (DSN)*. Veillez à ajouter cette variable à CircleCI et dans le fichier *.env*.

La journalisation Sentry peut être testée en naviguant vers `/sentry-debug/`.
Ce point de terminaison provoque une *ZeroDivisionError* ([exemple](https://jighart.sentry.io/share/issue/11b528e996cd49aba92671ea79a713d4/)).