# src/model/evaluate.py
from pathlib import Path
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from src.preprocessing.feature_engineering import build_training_matrices
from src.preprocessing.clean_data import RAW_DATA_PATH

MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"


def evaluate():
    print("📦 Chargement des données...")
    X, y, _ = build_training_matrices(RAW_DATA_PATH)

    print("📦 Chargement du modèle...")
    bundle = joblib.load(MODEL_PATH)
    model = bundle["model"]

    y_pred = model.predict(X)

    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    mae = mean_absolute_error(y, y_pred)

    print(f"R² global : {r2:.4f}")
    print(f"RMSE      : {rmse:.2f}")
    print(f"MAE       : {mae:.2f}")


if __name__ == "__main__":
    evaluate()
