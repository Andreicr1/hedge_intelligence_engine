import { Routes, Route } from "react-router-dom"
import Home from "./pages/Home"
import Simulador from "./pages/Simulador"
import SimuladorEstocastico from "./pages/SimuladorEstocastico"
import NotFound from "./pages/NotFound"

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/simular" element={<Simulador />} />
      <Route path="/simular-estocastico" element={<SimuladorEstocastico />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  )
}
