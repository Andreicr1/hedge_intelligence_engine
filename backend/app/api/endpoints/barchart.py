
from fastapi import APIRouter, Query
import xlwings as xw
import os

router = APIRouter()

@router.get("/read-symbol/")
def read_barchart_symbol(symbol: str = Query(..., description="Código do contrato (ex: P4Y00)")):
    try:
        excel_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "DataSheet.xlsx"))
        wb = xw.Book(excel_path)
        sht = wb.sheets['Planilha1']

        for row in range(5, 100):
            if sht.range(f"C{row}").value == symbol:
                return {
                    "symbol": symbol,
                    "name": sht.range(f"D{row}").value,
                    "last": sht.range(f"E{row}").value,
                    "change": sht.range(f"H{row}").value,
                    "percent_change": sht.range(f"I{row}").value,
                    "open": sht.range(f"N{row}").value,
                    "high": sht.range(f"O{row}").value,
                    "low": sht.range(f"P{row}").value,
                    "close": sht.range(f"Q{row}").value,
                    "volume": sht.range(f"R{row}").value,
                    "open_interest": sht.range(f"S{row}").value
                }
        return {"error": f"Código '{symbol}' não encontrado."}
    except Exception as e:
        return {"error": str(e)}
