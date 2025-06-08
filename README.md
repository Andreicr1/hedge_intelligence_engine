
# Hedge Intelligence Engine

Plataforma inteligente para análise, simulação e recomendação de estratégias de hedge com dados reais de mercado.

## Visão Geral

O Hedge Intelligence Engine interpreta situações de exposição a risco (como variações cambiais, commodities ou taxas) descritas pelo usuário e sugere estratégias de hedge adequadas. O sistema se conecta a dados reais de mercado, analisa o cenário e apresenta simulações e recomendações de forma clara e estratégica.

## Tecnologias Utilizadas

- **Backend**: FastAPI + xlwings + SQLite
- **Frontend**: React (Vite) + Tailwind CSS
- **Banco de Dados**: SQLite (com upgrade opcional para PostgreSQL)
- **Ambiente**: Docker e execução local standalone

## Como Executar Localmente

### Pré-requisitos

- Python 3.11+
- Node.js 18+
- Excel instalado (para leitura via plugin Barchart)
- Docker (opcional, para execução containerizada)

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker-compose up --build
```

## Estrutura de Diretórios

```
hedge_intelligence_engine/
├── backend/
│   ├── app/
│   │   ├── api/endpoints/
│   │   ├── core/
│   ├── requirements.txt
├── frontend/
│   └── src/
│       ├── components/
│       ├── pages/
├── data/
│   └── DataSheet.xlsx
```

## Funcionalidades

- Interpretação textual de exposição ao risco
- Leitura em tempo real de cotações a partir do Excel
- Sugestão de estratégias de hedge com base em regras e IA
- Visualização de simulações e comparação entre cenários
- Arquitetura pronta para multilíngue (PT/EN)

## Contribuições

Contribuições são bem-vindas. Siga os padrões definidos e abra um Pull Request com explicação clara da proposta.

## Licença

Uso privado e institucional. Direitos reservados ao autor.
