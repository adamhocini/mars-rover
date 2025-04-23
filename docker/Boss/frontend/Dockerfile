# Utiliser une image Node.js
FROM node:16

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY package.json ./
RUN npm install

COPY . .

# Exposer le port pour React
EXPOSE 3000

# Commande d'exécution
CMD ["npm", "start"]