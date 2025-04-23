# Utiliser une image Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Exposer le port pour Flask
EXPOSE 5000

# Commande d'exécution
CMD ["python", "app.py"]