import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from src.preprocessing.clean_data import clean_data
from src.preprocessing.feature_engineering import build_features

# IMPORTANT : le dataset est dans backend/data/raw/
DEFAULT_DATA_PATH = Path("data/raw/data_immobiliers.csv")

# On reste cohérent : le modèle est bien dans backend/src/model/
DEFAULT_MODEL_PATH = Path("src/model/model.pkl")

DEFAULT_TEST_SIZE = 0.3
DEFAULT_RANDOM_STATE = 42


def train_model(
    data_path: Path = DEFAULT_DATA_PATH,
    model_path: Path = DEFAULT_MODEL_PATH,
    test_size: float = DEFAULT_TEST_SIZE,
    random_state: int = DEFAULT_RANDOM_STATE,
) -> float:
    """Entraîne un modèle RandomForestRegressor."""

    print(f"📥 Chargement du dataset : {data_path}")
    data = pd.read_csv(data_path)

    print("🧹 Nettoyage des données…")
    data = clean_data(data, drop_rows_without_target=True)

    print("⚙️ Construction des features…")
    X, y = build_features(data, target_col="valeur_fonciere")

    # IMPORTANT : Remplacement des NaN pour éviter les crash sklearn
    X = X.fillna(0)
    y = y.fillna(0)

    # Suppression des colonnes complètement vides (100% NaN à l’origine)
    empty_cols = [col for col in X.columns if X[col].nunique() <= 1]
    if empty_cols:
        print(f"⚠️ Suppression de colonnes vides : {empty_cols}")
        X = X.drop(columns=empty_cols)

    print(f"🔍 Shape X: {X.shape}, Shape y: {y.shape}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    print("🚀 Entraînement du modèle RandomForest…")
    model = RandomForestRegressor(random_state=random_state)
    model.fit(X_train, y_train)

    print("📊 Évaluation du modèle…")
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print(f"🎯 R² sur le jeu de test : {r2:.4f}")

    print(f"💾 Sauvegarde du modèle dans : {model_path}")
    model_path = Path(model_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)

    return r2


def main():
    parser = argparse.ArgumentParser(description="Entraîner le modèle immobilier.")
    parser.add_argument(
        "--data-path",
        type=Path,
        default=DEFAULT_DATA_PATH,
        help="Chemin vers le fichier CSV brut.",
    )
    parser.add_argument(
        "--model-path",
        type=Path,
        default=DEFAULT_MODEL_PATH,
        help="Chemin de sortie pour le modèle entraîné.",
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=DEFAULT_TEST_SIZE,
        help="Taille du jeu de test (entre 0 et 1).",
    )
    parser.add_argument(
        "--random-state",
        type=int,
        default=DEFAULT_RANDOM_STATE,
        help="Graine aléatoire pour la reproductibilité.",
    )

    args = parser.parse_args()
    train_model(
        data_path=args.data_path,
        model_path=args.model_path,
        test_size=args.test_size,
        random_state=args.random_state,
    )


if __name__ == "__main__":
    main()
