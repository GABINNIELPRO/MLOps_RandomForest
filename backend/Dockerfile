FROM python:3.13-slim

# Répertoire de travail
WORKDIR /app

# Pour que Python trouve "api" et "src"
ENV PYTHONPATH="/app"

# Copier requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier TOUT le backend
COPY . .

# (Optionnel) Création du dossier modèle si nécessaire
RUN mkdir -p src/model

# ⚠️ Suppression de la vérification du modèle
# Le fichier model.pkl n'est plus dans le repo GitHub
# Il sera chargé autrement (S3, HuggingFace, Volume, Pipeline, etc.)
# RUN test -f src/model/model.pkl || (echo "❌ model.pkl manquant !" && exit 1)

# Exposer FastAPI
EXPOSE 8000

# Lancer FastAPI
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
