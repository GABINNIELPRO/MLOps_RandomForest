// src/lib/api.ts

// URL backend (chargée depuis .env.local)
export const API_BASE =
  import.meta.env.VITE_API_URL?.replace(/\/$/, "") || "http://localhost:8000";

// 🔎 Debug (AFFICHER dans la console du navigateur)
console.log("🔧 VITE_API_URL =", import.meta.env.VITE_API_URL);
console.log("🔧 API_BASE =", import.meta.env.VITE_API_URL?.replace(/\/$/, "") || "http://localhost:8000");


// ---------------------------------------------------
// Types EXACTEMENT comme PropertyFeatures du backend
// ---------------------------------------------------
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

// ----------------------------
// 🔹 Réponse du backend
// ----------------------------
export type PredictionResponse = {
  predicted_price: number;
};

// ----------------------------
// 🔹 Helper Fetch
// ----------------------------
async function jsonFetch<T>(url: string, options?: RequestInit): Promise<T> {
  try {
    const res = await fetch(url, options);

    if (!res.ok) {
      throw new Error(`Backend error ${res.status}: ${await res.text()}`);
    }

    return res.json() as Promise<T>;
  } catch (err) {
    console.error("❌ API ERROR:", err);
    throw new Error("Erreur de connexion au backend");
  }
}

// ----------------------------
// 🔥 Appel /predict
// ----------------------------
export async function predictPrice(
  input: PredictionInput
): Promise<PredictionResponse> {
  return jsonFetch(`${API_BASE}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(input),
  });
}
