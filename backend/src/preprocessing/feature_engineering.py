from __future__ import annotations

from typing import Optional, Tuple

import pandas as pd

FEATURE_COLUMNS = [
    'numero_disposition', 'adresse_numero', 'code_postal', 'code_departement',
    'numero_volume', 'lot1_numero', 'lot1_surface_carrez', 'lot2_numero',
    'lot2_surface_carrez', 'lot3_numero', 'lot3_surface_carrez',
    'lot4_numero', 'lot4_surface_carrez', 'lot5_numero',
    'lot5_surface_carrez', 'nombre_lots', 'surface_reelle_bati',
    'nombre_pieces_principales', 'surface_terrain', 'longitude', 'latitude',
    'lot1_numero_missing', 'lot1_surface_carrez_missing',
    'lot2_numero_missing', 'lot2_surface_carrez_missing',
    'lot3_numero_missing', 'lot3_surface_carrez_missing',
    'lot4_numero_missing', 'lot4_surface_carrez_missing',
    'lot5_numero_missing', 'lot5_surface_carrez_missing',
    'type_local_missing', 'surface_reelle_bati_missing',
    'nombre_pieces_principales_missing', 'surface_terrain_missing',
    'nature_culture_missing', 'missing_count', 'year', 'month', 'day',
    'nature_mutation_encoded', 'nom_commune_encoded',
    'adresse_nom_voie_encoded', 'nature_culture_encoded', 'type_local_encoded'
]

def add_date_features(data: pd.DataFrame) -> pd.DataFrame:
    """Ajoute des variables dérivées à partir de `date_mutation`."""
    if "date_mutation" not in data.columns:
        return data

    data = data.copy()
    data["date_mutation_converted"] = pd.to_datetime(data["date_mutation"])
    data["year"] = data["date_mutation_converted"].dt.year
    data["month"] = data["date_mutation_converted"].dt.month
    data["day"] = data["date_mutation_converted"].dt.day
    data = data.drop(columns=["date_mutation", "date_mutation_converted"])
    return data


def build_features(
    data: pd.DataFrame,
    target_col: str = "valeur_fonciere",
) -> Tuple[pd.DataFrame, Optional[pd.Series]]:
    """
    Crée la matrice de features X et éventuellement la cible y.

    - ajoute les features de date
    - convertit les colonnes numériques
    - encode les colonnes catégorielles par fréquence
    """
    data = add_date_features(data)

    has_target = target_col in data.columns
    if has_target:
        y = data[target_col].copy()
        X = data.drop(columns=[target_col]).copy()
    else:
        y = None
        X = data.copy()

    # Conversion des colonnes numériques
    numeric_columns = [
        "longitude",
        "latitude",
        "numero_volume",
        "lot1_numero",
        "lot1_surface_carrez",
        "lot2_numero",
        "lot2_surface_carrez",
        "lot3_numero",
        "lot3_surface_carrez",
        "lot4_numero",
        "lot4_surface_carrez",
        "lot5_numero",
        "lot5_surface_carrez",
        "surface_reelle_bati",
        "nombre_pieces_principales",
        "surface_terrain",
    ]
    for col in numeric_columns:
        if col in X.columns:
            X[col] = (
                pd.to_numeric(X[col], errors="coerce")
                .fillna(0)
                .astype(float)
            )

    # Encodage des colonnes catégorielles par fréquence
    categorical_columns = [
        "nature_mutation",
        "nom_commune",
        "adresse_nom_voie",
        "nature_culture",
        "type_local",
    ]
    for col in categorical_columns:
        if col in X.columns:
            freq = X[col].value_counts(normalize=True)
            X[col + "_encoded"] = X[col].map(freq)
            X = X.drop(columns=[col])  # on enlève la variable brute

    return X, y
