// src/lib/types.ts

/* --------------------------------------------
   📌 Structure EXACTEMENT identique à PropertyFeatures
   du backend FastAPI
---------------------------------------------*/
export type PredictionInput = {
  numero_disposition: number;
  adresse_numero: number;
  code_postal: number;
  code_departement: number;
  numero_volume: number;

  lot1_numero: number;
  lot1_surface_carrez: number;
  lot2_numero: number;
  lot2_surface_carrez: number;
  lot3_numero: number;
  lot3_surface_carrez: number;
  lot4_numero: number;
  lot4_surface_carrez: number;
  lot5_numero: number;
  lot5_surface_carrez: number;

  nombre_lots: number;
  surface_reelle_bati: number;
  nombre_pieces_principales: number;
  surface_terrain: number;
  longitude: number;
  latitude: number;

  lot1_numero_missing: number;
  lot1_surface_carrez_missing: number;
  lot2_numero_missing: number;
  lot2_surface_carrez_missing: number;
  lot3_numero_missing: number;
  lot3_surface_carrez_missing: number;
  lot4_numero_missing: number;
  lot4_surface_carrez_missing: number;
  lot5_numero_missing: number;
  lot5_surface_carrez_missing: number;

  type_local_missing: number;
  surface_reelle_bati_missing: number;
  nombre_pieces_principales_missing: number;
  surface_terrain_missing: number;
  nature_culture_missing: number;

  missing_count: number;
  year: number;
  month: number;
  day: number;

  nature_mutation_encoded: number;
  nom_commune_encoded: number;
  adresse_nom_voie_encoded: number;
  nature_culture_encoded: number;
  type_local_encoded: number;
};


/* --------------------------------------------
   📌 Structure renvoyée par FastAPI
---------------------------------------------*/
export type PredictionResponse = {
  predicted_price: number;
};
