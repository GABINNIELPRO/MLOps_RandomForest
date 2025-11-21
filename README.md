# 🏡 Projet Deep Learning – Prédiction Immobilière

**Date:** December 2024  
**Presented by:** Gabin Niel  

---

Ce projet a pour objectif de construire un modèle de deep learning capable de prédire la valeur foncière de biens immobiliers à partir d’un dataset public.
Le travail inclut : préparation des données, exploration, entraînement du modèle, puis déploiement complet sur une plateforme cloud avec un pipeline CI/CD professionnel.

🚀 Fonctionnalités principales

📊 Exploration et nettoyage des données

🧠 Modélisation Deep Learning (réseau de neurones)

🧪 Évaluation du modèle et visualisations

🌐 Déploiement d’une API backend pour servir le modèle

💻 Déploiement d’un frontend consommant l’API

⚙️ CI/CD automatisé

☁️ Infrastructure cloud entièrement sur AWS

🧠 Partie Deep Learning
1. Préparation des données

À partir du fichier data_immobiliers.csv :

Suppression des colonnes inutiles

Analyse des valeurs manquantes

Normalisation / encodage

2. Exploration

Distribution de la valeur foncière

Visualisations Matplotlib

3. Modélisation

Réseau de neurones dense (Keras/TensorFlow ou PyTorch selon ton notebook)

Split train/test

Courbes d’apprentissage

☁️ Architecture Cloud

L’application complète (modèle + API + frontend) a été déployée sur AWS.

🔹 Backend

Serveur FastAPI/Flask (selon ton choix)

Endpoint /predict servant le modèle

🔹 Frontend

Interface web simple permettant de saisir les valeurs et d’obtenir la prédiction

Déployé sur la même plateforme cloud

🗄️ Stockage du modèle

Le modèle entraîné est stocké dans Amazon S3

⚙️ CI/CD Automatisé

Un pipeline CI/CD complet a été mis en place :

🛠️ Build automatique des images (backend + frontend)

📦 Push vers Amazon ECR

🚀 Déploiement automatique sur Amazon ECS

🔒 Droits gérés avec IAM

📈 Logs et métriques via Amazon CloudWatch

📦 Services AWS utilisés
Service	Rôle
Amazon S3	Stockage du modèle
Amazon ECR	Registre Docker des images du backend et frontend
Amazon ECS (Fargate)	Exécution du backend et frontend
IAM	Gestion fine des permissions CI/CD et accès S3
CloudWatch	Logs, monitoring et alarmes
Load Balancer	Accès public à l’API / Frontend
🏗️ Structure du projet
.
├── data/
│   └── data_immobiliers.csv
├── notebook/
│   └── ProjetDeepLearning_GuindoSafieto.ipynb
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── model/
├── frontend/
│   └── ...
├── Dockerfile.backend
├── Dockerfile.frontend
└── README.md

▶️ Lancer le projet en local
Backend
cd backend
pip install -r requirements.txt
python app.py

Frontend

Selon ta stack (React / Vue / simple HTML) :

npm install
npm run dev

Docker (local)
docker compose up --build

🧪 Exemple d’appel API
curl -X POST "https://ton-api/predict" \
    -H "Content-Type: application/json" \
    -d '{"surface": 80, "nb_pieces": 3, "type_local":"Appartement"}'

📚 Notebook du projet

Le notebook complet d’analyse et de modélisation se trouve ici :
ProjetDeepLearning_GuindoSafieto.ipynb

📦 Améliorations futures

Ajout d’un modèle plus performant (XGBoost ou CNN tabulaire)

Monitoring ML (MLflow / SageMaker)

Dashboard d’analyse des prédictions
