from pathlib import Path

# Código da simulação estocástica com FastAPI, pandas, numpy e matplotlib
codigo_estocastico = ""
from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from uuid import uuid4
from pathlib import Path
from typing import Dict, Any

router = APIRouter()

class SimulacaoEstocasticaInput(BaseModel):
    preco_spot: float
    strike_put: float
    premio_put: float
    strike_call: float
    premio_call: float
    vol_anual: float
    dias: int
    caminhos: int

@router.post("/simular/estocastico/", response_model=Dict[str, Any])
def simular_estocastico(input: SimulacaoEstocasticaInput):
    S0 = input.preco_spot
    Kp = input.strike_put
    Pp = input.premio_put
    Kc = input.strike_call
    Pc = input.premio_call
    sigma = input.vol_anual
    T = input.dias / 252
    N = input.dias
    M = input.caminhos
    dt = T / N

    np.random.seed(42)
    Z = np.random.normal(0, 1, (M, N))
    S = np.zeros((M, N + 1))
    S[:, 0] = S0

    for t in range(1, N + 1):
        S[:, t] = S[:, t - 1] * np.exp(-0.5 * sigma**2 * dt + sigma * np.sqrt(dt) * Z[:, t - 1])

    ST = S[:, -1]
    payoff_put = np.maximum(Kp - ST, 0) - Pp
    payoff_call = -np.maximum(ST - Kc, 0) + Pc
    payoff_collar = payoff_put + payoff_call

    df = pd.DataFrame({
        "Preço Final": ST,
        "PUT": payoff_put,
        "CALL Vendida": payoff_call,
        "COLLAR": payoff_collar
    })

    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Caminhos simulados
    for i in range(min(50, M)):
        axs[0].plot(S[i], alpha=0.3)
    axs[0].set_title("Caminhos simulados de preço")
    axs[0].set_xlabel("Dias")
    axs[0].set_ylabel("Preço")

    # Distribuição de payoffs
    axs[1].hist([payoff_put, payoff_call, payoff_collar],
                bins=50, label=["PUT", "CALL", "COLLAR"], alpha=0.7)
    axs[1].set_title("Distribuição dos resultados")
    axs[1].set_xlabel("Resultado")
    axs[1].set_ylabel("Frequência")
    axs[1].legend()

    output_dir = Path("backend/app/static")
    output_dir.mkdir(parents=True, exist_ok=True)
    img_name = f"simulacao_estocastica_{uuid4().hex[:8]}.png"
    img_path = output_dir / img_name
    fig.tight_layout()
    fig.savefig(img_path, bbox_inches="tight")
    plt.close(fig)

    resumo = df.describe().to_dict()

    return {
        "grafico_url": f"/static/{img_name}",
        "resumo": resumo
    }

# Salvar o código como simular_estocastico.py
path = Path("backend/app/api/endpoints/simular_estocastico.py")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(codigo_estocastico.strip(), encoding="utf-8")

path.name
