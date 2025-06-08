
import React, { useState } from 'react'

function Interpretador() {
  const [descricao, setDescricao] = useState('')
  const [resultado, setResultado] = useState(null)
  const [erro, setErro] = useState(null)

  const interpretar = async () => {
    try {
      const res = await fetch('http://localhost:8000/interpretar/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ descricao })
      })
      const json = await res.json()
      setResultado(json)
      setErro(null)
    } catch (err) {
      setErro('Erro ao interpretar descrição.')
      setResultado(null)
    }
  }

  return (
    <div className="p-4">
      <h2 className="text-xl font-semibold mb-2">Interpretador de Exposição</h2>
      <textarea
        value={descricao}
        onChange={(e) => setDescricao(e.target.value)}
        placeholder="Descreva sua situação de risco..."
        className="w-full h-28 p-2 border border-gray-300 rounded mb-2"
      />
      <button
        onClick={interpretar}
        className="bg-green-600 text-white px-4 py-2 rounded"
      >
        Interpretar
      </button>

      {erro && <p className="text-red-500 mt-4">{erro}</p>}

      {resultado && (
        <div className="mt-4 bg-gray-100 p-4 rounded text-sm whitespace-pre-wrap">
          <p><strong>Ativo:</strong> {resultado.ativo}</p>
          <p><strong>Prazo:</strong> {resultado.prazo}</p>
          <p><strong>Moeda:</strong> {resultado.moeda}</p>
          <p><strong>Contrato:</strong> {resultado.contrato}</p>
          <p><strong>Risco subjetivo:</strong> {resultado.risco_subjetivo}</p>
          <p><strong>Tipo de risco:</strong> {resultado.tipo_de_risco}</p>
          <p><strong>Exposição:</strong> {resultado.exposição}</p>

          <p className="mt-2"><strong>Estratégias sugeridas:</strong></p>
          <ul className="list-disc ml-6">
            {resultado.estratégias_sugeridas.map((estrat, idx) => (
              <li key={idx}>{estrat}</li>
            ))}
          </ul>

          {resultado.explicacoes.length > 0 && (
            <>
              <p className="mt-4 font-semibold">Detalhes das Estratégias:</p>
              {resultado.explicacoes.map((exp, i) => (
                <div key={i} className="bg-white border rounded p-2 mt-2">
                  <p><strong>{exp.nome}</strong></p>
                  <p><em>O que é:</em> {exp.o_que_e}</p>
                  <p><em>Como funciona:</em> {exp.como_funciona}</p>
                  <p><em>Quando usar:</em> {exp.quando_usar}</p>
                  <p><em>Exemplo:</em> {exp.exemplo}</p>
                </div>
              ))}
            </>
          )}
        </div>
      )}
    </div>
  )
}

export default Interpretador
