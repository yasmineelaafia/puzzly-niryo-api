# Puzzly-Niryo-API

Ceci est un projet qui donne la main aux clients http de controller le robot **Niryo** avec des commandes vocales

## Preparation de l'environement de travail

### Virtual Environement

```
python -m venv .venv
```

Ceci crée un dossier **.venv** dans la racine du projet

### Activation de l'environement virtuel

__Sur Windows:__

```ps
.\.venv\Scripts\activate
```

__Sur Linux:__

```bash
source ./.venv/bin/activate
```

## Installation des packages

```
pip install -r requirements.txt
```

## Execution et lancement du serveur flask

```
flask run --with-threads --host=0.0.0.0 --port=5000
```

## Licence

Ce projet est livré sous licence GPL3, voir [LICENCE](./LICENCE)