export default function PredictionResult({ price }: { price: number | null }) {
  if (price === null) return null;

  return (
    <div className="mt-5 p-5 rounded-xl bg-green-100 border border-green-300">
      <h2 className="text-xl font-bold text-green-700">Prix estimé</h2>
      <p className="text-2xl font-bold text-green-800 mt-2">
        {price.toLocaleString()} €
      </p>
    </div>
  );
}
