# Telegram Bot (moneysim / telegram-bot)

Ce dossier contient un petit bot Telegram écrit en Python (`bot.py`) utilisant la librairie `python-telegram-bot`.

## Description

Le bot répond à quelques commandes simples :
- `/start` : message de bienvenue
- `/help` : aide
- Répond automatiquement aux messages texte (ex. "bonjour")

Le bot est actuellement configuré pour tourner en mode polling.

> Remarque de sécurité : le fichier `bot.py` contient un token Telegram en clair. Il est fortement recommandé d'utiliser une variable d'environnement pour stocker le token au lieu de le laisser en dur dans le code.

## Prérequis

- Python 3.8+ (préféré 3.10+)
- pip

Les dépendances listées dans `requirements.txt` :

- python-telegram-bot==22.5

## Installation

Ouvrez PowerShell dans le dossier `telegram-bot` puis créez un environnement virtuel (optionnel) et installez les dépendances :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuration (token Telegram)

Il faut fournir un token d'API Telegram (issu de @BotFather). Plutôt que d'éditer le fichier `bot.py`, définissez une variable d'environnement `TELEGRAM_TOKEN` et modifiez le code pour l'utiliser (ou remplacez la valeur dans `bot.py` si vous préférez, mais évitez de commit le token).

Exemple (PowerShell) :

```powershell
$env:TELEGRAM_TOKEN = "<votre_token_ici>"
python .\bot.py
```

Si vous souhaitez modifier `bot.py` pour lire la variable d'environnement, un changement simple consiste à remplacer la constante `TOKEN = "..."` par :

```python
import os
TOKEN = os.environ.get("TELEGRAM_TOKEN")
```

Assurez-vous ensuite de ne pas committer le token dans le dépôt.

## Exécution

Lancement en local (après avoir défini `TELEGRAM_TOKEN` ou remplacé le token dans `bot.py`) :

```powershell
python .\bot.py
```

Le bot utilise le polling et affichera un message de démarrage dans la console.

## Utilisation

- Envoyez `/start` au bot pour recevoir le message de bienvenue.
- Envoyez un message texte (par exemple "bonjour") et le bot répondra.

## Notes et améliorations suggérées

- Remplacer le token hardcodé par l'utilisation d'une variable d'environnement (sécurité).
- Ajouter un fichier `.env` (avec `python-dotenv`) et l'ignorer via `.gitignore` si vous préférez la gestion locale.
- Mettre en place un service/systemd (Linux) ou un conteneur Docker pour le déploiement.
- Ajouter des tests unitaires et un CI simple si besoin.

## Licence

Vérifiez la licence principale du dépôt. Ce dossier hérite de la même licence que le projet racine (si présent).

## Contact

Pour questions ou améliorations, ouvrez une issue ou contactez le mainteneur du dépôt.
