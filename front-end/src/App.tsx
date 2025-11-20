import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Prediction from "./pages/Prediction";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/prediction" replace />} />
        <Route path="/prediction" element={<Prediction />} />
      </Routes>
    </BrowserRouter>
  );
}
