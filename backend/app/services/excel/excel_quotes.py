from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.core import barchart_bridge

router = APIRouter()

class ExcelRequest(BaseModel):
    codigos: List[str]
    campos: List[str]
    destino: str = "Quotes"

@router.post("/excel/quotes/")
def obter_dados_excel(request: ExcelRequest):
    try:
        dados = barchart_bridge.carregar_quotes_em_excel(
            codigos=request.codigos,
            campos=request.campos,
            destino=request.destino
        )
        return {"dados": dados}
    except Exception as e:
        return {"erro": str(e)}
