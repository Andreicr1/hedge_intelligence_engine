
import re
from typing import Dict

REGRAS_HEDGE = [
    {
        "tipo_de_risco": "preço",
        "exposição": "venda futura",
        "palavras_chave": ["venda", "queda", "preço baixo", "entregar", "receber"],
        "estratégias": ["fixar preço via swap", "comprar PUT", "fazer collar"]
    },
    {
        "tipo_de_risco": "preço",
        "exposição": "compra futura",
        "palavras_chave": ["compra", "subida", "insumo", "preço alto", "custo"],
        "estratégias": ["comprar CALL", "estratégia de CAP", "fixar preço com fornecedor"]
    },
    {
        "tipo_de_risco": "câmbio",
        "exposição": "recebimento em moeda estrangeira",
        "palavras_chave": ["receber em dólar", "exportar", "pagamento externo"],
        "estratégias": ["venda a termo de moeda", "opção de venda (PUT cambial)", "swap cambial passivo"]
    },
    {
        "tipo_de_risco": "basis",
        "exposição": "estoque com venda futura",
        "palavras_chave": ["basis", "spread", "arbitragem", "armazenado", "estoque"],
        "estratégias": ["travar basis via contrato basis", "usar futuros como proxy", "fixação local com hedge internacional"]
    },
    {
        "tipo_de_risco": "frete/energia",
        "exposição": "custo de transporte ou combustível",
        "palavras_chave": ["diesel", "frete", "custo logístico", "gás", "transporte"],
        "estratégias": ["fixar preço via contrato de fornecimento", "comprar CALL sobre energia", "indexar contratos"]
    }
]

EXPLICACOES_ESTRATEGIAS = {
    "fixar preço via swap": {
        "o_que_e": "Um contrato financeiro que transforma preço variável em fixo.",
        "como_funciona": "Você concorda em pagar/receber a diferença entre um preço fixo e o preço de mercado futuro.",
        "quando_usar": "Quando quiser previsibilidade total de preço.",
        "exemplo": "Fixar venda de alumínio a USD 2.300 por tonelada por 3 meses via swap com contraparte."
    },
    "comprar PUT": {
        "o_que_e": "Opção que dá direito de vender a um preço mínimo.",
        "como_funciona": "Se o preço cair abaixo do strike, você exerce a PUT e limita a perda.",
        "quando_usar": "Quando deseja proteção contra queda com potencial de ganho se o preço subir.",
        "exemplo": "Compra de PUT strike USD 2.200: se o preço cair abaixo disso, você tem proteção."
    },
    "fazer collar": {
        "o_que_e": "Estratégia que combina uma PUT (compra) com CALL (venda).",
        "como_funciona": "Protege abaixo do strike da PUT e limita ganhos acima do strike da CALL.",
        "quando_usar": "Quando quer hedge de custo reduzido com faixa de proteção.",
        "exemplo": "PUT strike 2200 e CALL strike 2500: protege abaixo de 2200, limita ganhos acima de 2500."
    }
    # outras estratégias podem ser adicionadas conforme necessário
}

def extrair_info(texto: str) -> Dict:
    texto = texto.lower()
    ativo = re.findall(r"(alum[ií]nio|milho|soja|diesel|g[aá]s|frete|usd|euro|real|cobre)", texto)
    prazo = re.findall(r"(setembro|outubro|novembro|dezembro|\d{1,2}/\d{1,2}/\d{2,4}|q[1-4]|\d+ dias?)", texto)
    moeda = re.findall(r"(usd|d[oó]lar|real|euro)", texto)
    contrato = re.findall(r"(spot|f[ií]sico|futuro|a termo)", texto)
    emocional = re.findall(r"(volatilidade|risco|preocupad[oa]|incerteza|medo)", texto)

    return {
        "ativo": ativo[0] if ativo else "não identificado",
        "prazo": prazo[0] if prazo else "não identificado",
        "moeda": moeda[0] if moeda else "não identificada",
        "contrato": contrato[0] if contrato else "não identificado",
        "risco_subjetivo": emocional[0] if emocional else "não identificado"
    }

def interpretar_descricao(texto: str) -> Dict:
    texto_lower = texto.lower()
    resultado = extrair_info(texto)
    resultado["descricao"] = texto
    resultado["tipo_de_risco"] = "não identificado"
    resultado["exposição"] = "não identificada"
    resultado["estratégias_sugeridas"] = []
    resultado["explicacoes"] = []

    for regra in REGRAS_HEDGE:
        if any(p in texto_lower for p in regra["palavras_chave"]):
            resultado["tipo_de_risco"] = regra["tipo_de_risco"]
            resultado["exposição"] = regra["exposição"]
            resultado["estratégias_sugeridas"] = regra["estratégias"]
            resultado["explicacoes"] = [
                {"nome": e, **EXPLICACOES_ESTRATEGIAS.get(e, {})}
                for e in regra["estratégias"] if e in EXPLICACOES_ESTRATEGIAS
            ]
            break

    return resultado
