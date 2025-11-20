from __future__ import annotations

import pandas as pd

COLUMNS_TO_DROP = [
    "id_mutation",
    "nature_culture_speciale",
    "code_nature_culture_speciale",
    "ancien_code_commune",
    "ancien_nom_commune",
    "ancien_id_parcelle",
    "adresse_suffixe",
    "code_commune",
    "code_type_local",
    "code_nature_culture",
    "section_prefixe",
    "adresse_code_voie",
]


def clean_data(
    data: pd.DataFrame,
    target_col: str = "valeur_fonciere",
    drop_rows_without_target: bool = True,
) -> pd.DataFrame:
    """
    Nettoie le DataFrame brut.

    - supprime les colonnes inutiles
    - gère les valeurs manquantes importantes
    - traite l'adresse, le code postal et les colonnes de lot

    Parameters
    ----------
    data : pd.DataFrame
        Données brutes.
    target_col : str
        Nom de la variable cible.
    drop_rows_without_target : bool
        Si True, supprime les lignes où la cible est manquante.

    Returns
    -------
    pd.DataFrame
        Données nettoyées.
    """
    data = data.copy()

    # Suppression de colonnes jugées non pertinentes
    existing_to_drop = [c for c in COLUMNS_TO_DROP if c in data.columns]
    if existing_to_drop:
        data = data.drop(columns=existing_to_drop)

    # Cible et infos d'adresse indispensables
    subset_cols = []
    if drop_rows_without_target and target_col in data.columns:
        subset_cols.append(target_col)
    if "adresse_nom_voie" in data.columns:
        subset_cols.append("adresse_nom_voie")
    if subset_cols:
        data = data.dropna(subset=subset_cols)

    # Adresse numéro : conversion en numérique puis remplissage par médiane
    if "adresse_numero" in data.columns and "adresse_nom_voie" in data.columns:
        data["adresse_numero"] = pd.to_numeric(
            data["adresse_numero"], errors="coerce"
        )
        data["adresse_numero"] = data.groupby("adresse_nom_voie")[
            "adresse_numero"
        ].transform(lambda x: x.fillna(x.median()))

    # Code postal : conversion en numérique puis remplissage par le mode dans chaque parcelle
    if "code_postal" in data.columns:
        data["code_postal"] = pd.to_numeric(data["code_postal"], errors="coerce")
        if "id_parcelle" in data.columns:

            def _fill_mode(series: pd.Series) -> pd.Series:
                mode = series.mode()
                fill_value = mode.iloc[0] if not mode.empty else series.median()
                return series.fillna(fill_value)

            data["code_postal"] = (
                data.groupby("id_parcelle")["code_postal"]
                .transform(_fill_mode)
            )

    # Traitement des colonnes lot{i}_numero et lot{i}_surface_carrez
    for i in range(1, 6):
        lot_numero_col = f"lot{i}_numero"
        lot_surface_col = f"lot{i}_surface_carrez"

        if lot_numero_col in data.columns:
            data[f"{lot_numero_col}_missing"] = (
                data[lot_numero_col].isnull().astype(int)
            )
            data[lot_numero_col] = data[lot_numero_col].fillna(-1)

        if lot_surface_col in data.columns:
            data[f"{lot_surface_col}_missing"] = (
                data[lot_surface_col].isnull().astype(int)
            )
            data[lot_surface_col] = data[lot_surface_col].fillna(0.0)

    # Lignes avec des valeurs manquantes critiques
    critical_cols = [
        col
        for col in ["latitude", "longitude", "adresse_numero"]
        if col in data.columns
    ]
    if critical_cols:
        data = data.dropna(subset=critical_cols)

    # id_parcelle ne sert plus après agrégation
    if "id_parcelle" in data.columns:
        data = data.drop(columns=["id_parcelle"])

    # Colonnes avec indicateurs de valeurs manquantes
    missing_columns = [
        col
        for col in [
            "type_local",
            "surface_reelle_bati",
            "nombre_pieces_principales",
            "surface_terrain",
            "nature_culture",
        ]
        if col in data.columns
    ]
    for col in missing_columns:
        data[f"{col}_missing"] = data[col].isnull().astype(int)
        if col == "surface_reelle_bati":
            data[col] = data[col].fillna(0)
        else:
            data[col] = data[col].fillna(-1)

    # Nombre total de valeurs manquantes encodées
    missing_flag_cols = [c for c in data.columns if c.endswith("_missing")]
    if missing_flag_cols:
        data["missing_count"] = data[missing_flag_cols].sum(axis=1)

    return data
