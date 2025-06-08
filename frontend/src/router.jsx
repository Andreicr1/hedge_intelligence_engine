import { createBrowserRouter, RouterProvider } from "react-router-dom"
import App from "@/App"
import Simulador from "@/pages/Simulador"
import SimuladorEstocastico from "@/pages/SimuladorEstocastico"
import NotFound from "@/pages/NotFound"

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/simular",
    element: <Simulador />,
  },
  {
    path: "/simular-estocastico",
    element: <SimuladorEstocastico />,
  },
  {
    path: "*",
    element: <NotFound />,
  },
])

export default function AppRouter() {
  return <RouterProvider router={router} />
}
