import { Link } from "react-router-dom"

export default function NotFound() {
  return (
    <div className="p-6 text-center">
      <h1 className="text-4xl font-bold text-red-600 mb-4">404</h1>
      <p className="text-gray-700 mb-4">Página não encontrada.</p>
      <Link to="/" className="text-blue-600 underline">Voltar para a página inicial</Link>
    </div>
  )
}

