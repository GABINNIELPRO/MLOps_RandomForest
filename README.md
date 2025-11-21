🏡 Projet Deep Learning – Prédiction Immobilière

Date : December 2024
Presented by : Gabin Niel

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

Réseau de neurones dense (Keras/TensorFlow ou PyTorch selon le notebook)

Split train/test

Courbes d’apprentissage

☁️ Architecture Cloud

L’application complète (modèle + API + frontend) a été déployée sur AWS.

🔹 Backend

Serveur FastAPI / Flask

Endpoint /predict servant le modèle

🔹 Frontend

Interface web permettant de saisir les valeurs et visualiser la prédiction

Déployé via ECS Fargate

🗄️ Stockage du modèle

Le modèle est stocké dans Amazon S3

⚙️ CI/CD Automatisé

Un pipeline complet CI/CD a été mis en place :

🛠️ Build automatique des images (backend + frontend)

📦 Push vers Amazon ECR

🚀 Déploiement automatique sur Amazon ECS

🔒 Gestion des droits via IAM

📈 Logs et monitoring via CloudWatch

📦 Services AWS utilisés
Service	Rôle
Amazon S3	Stockage du modèle
Amazon ECR	Registre Docker
Amazon ECS (Fargate)	Exécution backend + frontend
IAM	Permissions CI/CD & accès S3
CloudWatch	Logs & monitoring
Load Balancer	Accès public
🌍 Démo en ligne

👉 Projet déployé :

🔗 http://54.199.207.13/
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
