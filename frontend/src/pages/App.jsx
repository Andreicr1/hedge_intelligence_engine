
import React, { useState } from 'react'

function App() {
  const [symbol, setSymbol] = useState('')
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)

  const handleFetch = async () => {
    try {
      const res = await fetch(`http://localhost:8000/read-symbol/?symbol=${symbol}`)
      const json = await res.json()
      if (json.error) {
        setError(json.error)
        setData(null)
      } else {
        setData(json)
        setError(null)
      }
    } catch (err) {
      setError('Erro ao buscar dados.')
    }
  }

  return (
    <div className="p-4 font-sans">
      <h1 className="text-2xl font-bold mb-4">Hedge Intelligence Engine</h1>
      <input
        type="text"
        placeholder="Digite o código do contrato (ex: P4Y00)"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
        className="border px-2 py-1 mr-2"
      />
      <button onClick={handleFetch} className="bg-blue-500 text-white px-4 py-1 rounded">
        Buscar
      </button>

      {error && <p className="text-red-500 mt-4">{error}</p>}
      {data && (
        <pre className="mt-4 bg-gray-100 p-2 rounded text-sm">
          {JSON.stringify(data, null, 2)}
        </pre>
      )}
    </div>
  )
}

export default App
