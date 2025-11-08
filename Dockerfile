# Étape 1 : base Python
FROM python:3.11-slim

# Étape 2 : définir le répertoire de travail
WORKDIR /

# Étape 3 : copier les fichiers du projet
COPY requirements.txt requirements.txt
COPY app/bot.py app/bot.py

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8050

# Étape 5 : exécuter le bot
CMD ["python", "app/bot.py"]
