import argparse
from pathlib import Path

import joblib
import pandas as pd

from src.preprocessing.clean_data import clean_data
from src.preprocessing.feature_engineering import build_features

DEFAULT_MODEL_PATH = Path("src/model/model.pkl")


def predict_from_csv(
    csv_path: Path,
    model_path: Path = DEFAULT_MODEL_PATH,
) -> pd.DataFrame:
    """Charge un CSV, applique le prétraitement et renvoie les prédictions.

    Parameters
    ----------
    csv_path : Path
        Chemin vers le fichier CSV à prédire.
    model_path : Path
        Chemin du modèle entraîné (.pkl).

    Returns
    -------
    pd.DataFrame
        Données d'entrée avec une colonne supplémentaire
        'valeur_fonciere_pred'.
    """
    csv_path = Path(csv_path)
    model_path = Path(model_path)

    data = pd.read_csv(csv_path)
    data_clean = clean_data(data, drop_rows_without_target=False)
    X, _ = build_features(data_clean, target_col="valeur_fonciere")

    model = joblib.load(model_path)
    y_pred = model.predict(X)

    result = data_clean.copy()
    result["valeur_fonciere_pred"] = y_pred

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Prédictions de valeur foncière à partir d'un CSV."
    )
    parser.add_argument(
        "csv_path",
        type=Path,
        help="Chemin vers le fichier CSV à prédire.",
    )
    parser.add_argument(
        "--model-path",
        type=Path,
        default=DEFAULT_MODEL_PATH,
        help="Chemin du modèle entraîné (.pkl).",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=None,
        help="Chemin de sortie pour sauvegarder le CSV avec les prédictions.",
    )

    args = parser.parse_args()

    result = predict_from_csv(args.csv_path, model_path=args.model_path)

    if args.output_path is not None:
        args.output_path.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(args.output_path, index=False)
        print(f"Résultats sauvegardés dans {args.output_path}")
    else:
        print(result.head())


if __name__ == "__main__":
    main()
