import { useState } from "react";
import InputField from "./InputField";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function PredictionForm({
  onResult,
}: {
  onResult: (value: number) => void;
}) {
  const [form, setForm] = useState({
    numero_disposition: 0,
    adresse_numero: 0,
    code_postal: 0,
    code_departement: 0,
    numero_volume: 0,

    lot1_numero: 0,
    lot1_surface_carrez: 0,
    lot2_numero: 0,
    lot2_surface_carrez: 0,
    lot3_numero: 0,
    lot3_surface_carrez: 0,
    lot4_numero: 0,
    lot4_surface_carrez: 0,
    lot5_numero: 0,
    lot5_surface_carrez: 0,

    nombre_lots: 0,
    surface_reelle_bati: 0,
    nombre_pieces_principales: 0,
    surface_terrain: 0,
    longitude: 0,
    latitude: 0,

    lot1_numero_missing: 0,
    lot1_surface_carrez_missing: 0,
    lot2_numero_missing: 0,
    lot2_surface_carrez_missing: 0,
    lot3_numero_missing: 0,
    lot3_surface_carrez_missing: 0,
    lot4_numero_missing: 0,
    lot4_surface_carrez_missing: 0,
    lot5_numero_missing: 0,
    lot5_surface_carrez_missing: 0,

    type_local_missing: 0,
    surface_reelle_bati_missing: 0,
    nombre_pieces_principales_missing: 0,
    surface_terrain_missing: 0,
    nature_culture_missing: 0,

    missing_count: 0,
    year: 2020,
    month: 1,
    day: 1,

    nature_mutation_encoded: 0,
    nom_commune_encoded: 0,
    adresse_nom_voie_encoded: 0,
    nature_culture_encoded: 0,
    type_local_encoded: 0,
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  async function handleSubmit() {
    const body = Object.fromEntries(
      Object.entries(form).map(([k, v]) => [k, Number(v)])
    );

    const res = await fetch(`${API}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const data = await res.json();
    onResult(data.predicted_price);
  }

  return (
    <div className="space-y-4">
      {Object.keys(form).map((field) => (
        <InputField
          key={field}
          label={field}
          name={field}
          value={form[field as keyof typeof form]}
          onChange={handleChange}
        />
      ))}

      <button
        onClick={handleSubmit}
        className="w-full bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-xl font-bold"
      >
        Prédire
      </button>
    </div>
  );
}
