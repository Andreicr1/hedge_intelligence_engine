from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Endpoints da aplicação
from app.api.endpoints.barchart import router as barchart_router
from app.api.endpoints.simular import router as simulador_router
from app.api.endpoints.simular_estocastico import router as estocastico_router
from app.api.endpoints.interpretador_router import router as interpretador_router
from app.services.excel.excel_executor import router as excel_router

# Serviços Excel (rotas internas ou administrativas)
from app.services.excel.excel_executor import router as exec_funcao_router
from app.services.excel.excel_quotes import router as excel_router

# Inicializa app
app = FastAPI(title="Hedge Intelligence Engine API")

# Registra rotas
app.include_router(barchart_router)
app.include_router(simulador_router)
app.include_router(estocastico_router)
app.include_router(interpretador_router)
app.include_router(exec_funcao_router)
app.include_router(excel_router)

# Servir arquivos estáticos (ex: gráficos salvos)
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
