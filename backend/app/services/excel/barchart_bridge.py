# backend/app/services/excel/barchart_bridge.py

import xlwings as xw
import pandas as pd
import time
from typing import List

def carregar_quotes_em_excel(codigos: List[str], campos: List[str], destino: str = "Quotes"):
    wb = xw.apps.active.books.active
    sht = wb.sheets[destino]

    formula = f'=BCQ("{",".join(codigos)}", "{",".join(campos)}", "futures")'
    sht.range("A1").formula = formula

    time.sleep(2)  # ajuste conforme desempenho

    df = sht.range("A1").expand().options(pd.DataFrame, header=True, index=False).value
    return df.to_dict(orient="records")
