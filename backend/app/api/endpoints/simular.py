from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from uuid import uuid4
from pathlib import Path

router = APIRouter()

class SimulacaoInput(BaseModel):
    preco_spot: float
    strike_put: float
    premio_put: float
    strike_call: float
    premio_call: float

@router.post("/simular/")
def simular_endpoint(input: SimulacaoInput):
    spot = input.preco_spot
    k_put = input.strike_put
    p_put = input.premio_put
    k_call = input.strike_call
    p_call = input.premio_call

    precos = np.linspace(spot * 0.7, spot * 1.3, 100)
    df = pd.DataFrame({"preco_mercado": precos})

    # Estratégia 1: somente PUT
    df["put"] = np.where(df["preco_mercado"] < k_put,
                         k_put - df["preco_mercado"], 0) - p_put

    # Estratégia 2: somente CALL vendida
    df["call_vendida"] = -np.where(df["preco_mercado"] > k_call,
                                   df["preco_mercado"] - k_call, 0) + p_call

    # Estratégia 3: COLLAR = PUT comprada + CALL vendida
    df["collar"] = df["put"] + df["call_vendida"]

    # Gera gráfico
    fig, ax = plt.subplots()
    ax.plot(df["preco_mercado"], df["put"], label="PUT")
    ax.plot(df["preco_mercado"], df["call_vendida"], label="CALL vendida")
    ax.plot(df["preco_mercado"], df["collar"], label="COLLAR")
    ax.axhline(0, color='gray', linewidth=0.8)
    ax.set_xlabel("Preço do mercado")
    ax.set_ylabel("Resultado do hedge")
    ax.legend()
    ax.grid(True)

    output_dir = Path("backend/app/static")
    output_dir.mkdir(parents=True, exist_ok=True)
    img_name = f"simulacao_{uuid4().hex[:8]}.png"
    img_path = output_dir / img_name
    fig.savefig(img_path, bbox_inches="tight")
    plt.close(fig)

    return {
        "grafico_url": f"/static/{img_name}",
        "dados": df[["preco_mercado", "put", "call_vendida", "collar"]].to_dict(orient="records")
    }
