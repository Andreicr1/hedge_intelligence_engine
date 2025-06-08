import { Link } from "react-router-dom"

export default function Home() {
  return (
    <main className="p-8 max-w-xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">Hedge Intelligence Engine</h1>

      <p className="mb-4 text-gray-700 text-center">
        Selecione uma das simulações disponíveis:
      </p>

      <div className="flex flex-col gap-4">
        <Link
          to="/simular"
          className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg text-center font-semibold shadow"
        >
          Simulador Determinístico
        </Link>

        <Link
          to="/simular-estocastico"
          className="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-lg text-center font-semibold shadow"
        >
          Simulador Estocástico
        </Link>

        <Link
          to="/excel-quotes"
          className="bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg text-center font-semibold shadow"
        >
          Consultar Dados Excel (via Plugin Barchart)
        </Link>
      </div>
    </main>
  )
}
