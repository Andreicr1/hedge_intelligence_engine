
from fastapi import APIRouter
from pydantic import BaseModel
from .interpretador import interpretar_descricao

router = APIRouter()

class TextoInput(BaseModel):
    descricao: str

@router.post("/interpretar/")
def interpretar(input: TextoInput):
    resultado = interpretar_descricao(input.descricao)
    return resultado
