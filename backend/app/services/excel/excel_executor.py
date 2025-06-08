from pathlib import Path

# Código do endpoint que conecta com o bridge
codigo_endpoint = "cd.."
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Literal
import pandas as pd

from app.services.excel import barchart_bridge as bridge

router = APIRouter()

class ExecFuncaoInput(BaseModel):
    funcao: Literal["quotes", "forward_curve", "historico"]
    codigos: List[str] = []
    colunas: List[str] = []
    aba: str = "Quotes"  # Default, pode ser "History" ou "ForwardCurve"

@router.post("/barchart/exec-funcao")
def executar_funcao(input: ExecFuncaoInput):
    try:
        if input.funcao == "quotes":
            df = bridge.buscar_quotes(input.codigos, input.colunas)
        elif input.funcao == "forward_curve":
            df = bridge.buscar_forward_curve(input.aba)
        elif input.funcao == "historico":
            df = bridge.buscar_historico(input.aba)
        else:
            raise HTTPException(status_code=400, detail="Função inválida")
        
        return {
            "colunas": df.columns.tolist(),
            "dados": df.to_dict(orient="records")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Caminho de destino do novo endpoint
endpoint_path = Path("/mnt/data/exec_funcao.py")
endpoint_path.write_text(codigo_endpoint, encoding="utf-8")

endpoint_path
