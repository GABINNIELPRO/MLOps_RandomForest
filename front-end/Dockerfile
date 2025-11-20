###########################
# Étape 1 — Build
###########################
FROM node:18 AS build

WORKDIR /app

# Copier uniquement les fichiers nécessaires pour installer les deps
COPY package*.json ./

# Installation des dépendances, y compris dev (vite)
RUN npm ci --include=dev --silent

# Copier le code SAUF node_modules
COPY . .

# ⚠️ Supprimer node_modules si ton COPY les écrase (Windows)
RUN rm -rf node_modules

# Réinstaller proprement après le COPY (fix la vraie cause)
RUN npm ci --include=dev --silent

# Build Vite
RUN npm run build

###########################
# Étape 2 — Nginx
###########################
FROM nginx:stable-alpine

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
