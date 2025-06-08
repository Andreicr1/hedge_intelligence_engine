import { useState } from "react";

export default function ExcelQuotes() {
  const [loading, setLoading] = useState(false);
  const [dados, setDados] = useState([]);
  const [erro, setErro] = useState(null);

  const testarExcel = async () => {
    setLoading(true);
    setErro(null);
    setDados([]);

    try {
      const response = await fetch("http://localhost:8000/excel/quotes/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          codigos: ["ALIU24"],
          campos: ["Last", "Volume"]
        })
      });

      if (!response.ok) {
        throw new Error(`Erro ${response.status}`);
      }

      const data = await response.json();
      setDados(data);
    } catch (err: any) {
      setErro(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 rounded-xl shadow bg-white max-w-xl mx-auto mt-6">
      <h2 className="text-xl font-semibold mb-4">Testar integração com Excel</h2>
      <button
        className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        onClick={testarExcel}
        disabled={loading}
      >
        {loading ? "Consultando..." : "Consultar Excel (ALIU24)"}
      </button>

      {erro && <p className="mt-4 text-red-500">Erro: {erro}</p>}

      {dados.length > 0 && (
        <table className="mt-4 w-full border text-sm">
          <thead>
            <tr>
              {Object.keys(dados[0]).map((key) => (
                <th key={key} className="border px-2 py-1 bg-gray-100">
                  {key}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {dados.map((linha, i) => (
              <tr key={i}>
                {Object.values(linha).map((val, j) => (
                  <td key={j} className="border px-2 py-1">
                    {val}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
