// src/pages/Prediction.tsx

import { useState } from "react";
import PredictionForm from "../components/PredictionForm";
import PredictionResult from "../components/PredictionResult";

export default function Prediction() {
  const [price, setPrice] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">
        📈 Prédiction du prix immobilier
      </h1>

      {/* FORMULAIRE */}
      <PredictionForm
        loading={loading}
        onStart={() => setLoading(true)}
        onResult={(p) => {
          setPrice(p);
          setLoading(false);
        }}
        onError={() => setLoading(false)}
      />

      {/* RÉSULTAT */}
      <PredictionResult price={price} loading={loading} />
    </div>
  );
}
