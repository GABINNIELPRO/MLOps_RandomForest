import sys
import os

# Ajouter le dossier racine du projet au PYTHONPATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT_DIR)

from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.preprocessing.feature_engineering import FEATURE_COLUMNS



app = FastAPI(
    title="Immo Price Predictor API",
    version="1.0.0",
    description="API de prédiction de valeur foncière."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📌 Chemin du modèle
MODEL_PATH = Path(__file__).resolve().parents[1] / "src" / "model" / "model.pkl"
_model = joblib.load(MODEL_PATH)

# — le reste du fichier ensuite —



# 📌 👉 ICI tu mets ta classe PropertyFeatures
class PropertyFeatures(BaseModel):
    numero_disposition: float = 0
    adresse_numero: float = 0
    code_postal: float = 0
    code_departement: float = 0
    numero_volume: float = 0

    lot1_numero: float = 0
    lot1_surface_carrez: float = 0
    lot2_numero: float = 0
    lot2_surface_carrez: float = 0
    lot3_numero: float = 0
    lot3_surface_carrez: float = 0
    lot4_numero: float = 0
    lot4_surface_carrez: float = 0
    lot5_numero: float = 0
    lot5_surface_carrez: float = 0

    nombre_lots: float = 0
    surface_reelle_bati: float = 0
    nombre_pieces_principales: float = 0
    surface_terrain: float = 0
    longitude: float = 0
    latitude: float = 0

    lot1_numero_missing: float = 0
    lot1_surface_carrez_missing: float = 0
    lot2_numero_missing: float = 0
    lot2_surface_carrez_missing: float = 0
    lot3_numero_missing: float = 0
    lot3_surface_carrez_missing: float = 0
    lot4_numero_missing: float = 0
    lot4_surface_carrez_missing: float = 0
    lot5_numero_missing: float = 0
    lot5_surface_carrez_missing: float = 0

    type_local_missing: float = 0
    surface_reelle_bati_missing: float = 0
    nombre_pieces_principales_missing: float = 0
    surface_terrain_missing: float = 0
    nature_culture_missing: float = 0

    missing_count: float = 0
    year: float = 0
    month: float = 0
    day: float = 0

    nature_mutation_encoded: float = 0
    nom_commune_encoded: float = 0
    adresse_nom_voie_encoded: float = 0
    nature_culture_encoded: float = 0
    type_local_encoded: float = 0


class PredictionResponse(BaseModel):
    predicted_price: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(features: PropertyFeatures):

    row = [getattr(features, col) for col in FEATURE_COLUMNS]
    df = pd.DataFrame([row], columns=FEATURE_COLUMNS)

    pred = _model.predict(df)[0]
    return PredictionResponse(predicted_price=float(pred))
