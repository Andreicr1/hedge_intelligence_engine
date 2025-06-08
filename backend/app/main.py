from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.endpoints.barchart import router as barchart_router
from app.api.endpoints.simular import router as simulador_router
from app.api.endpoints.interpretador_router import router as interpretador_router

app = FastAPI(title="Hedge Intelligence Engine API")

# Rotas principais
app.include_router(barchart_router)
app.include_router(simulador_router)
app.include_router(interpretador_router)

# Servir imagens do simulador
from pathlib import Path
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
