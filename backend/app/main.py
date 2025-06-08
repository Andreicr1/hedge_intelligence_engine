
from fastapi import FastAPI
from app.api.endpoints.barchart import router as barchart_router

app = FastAPI(title="Hedge Intelligence Engine API")

app.include_router(barchart_router)

@app.get("/")
def read_root():
    return {"message": "API funcionando corretamente"}
