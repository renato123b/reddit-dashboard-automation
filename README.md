# 🚀 Reddit Top Posts Automation & Dashboard

Um ecossistema automatizado desenvolvido para minerar, processar e exibir de forma elegante os posts de maior engajamento do Reddit, focando especificamente em subreddits técnicos e de automação (`r/n8n` e `r/automation`).

Este projeto é dividido em um motor de scraping em Python extremamente rápido e um Dashboard Web moderno (estilo *dark theme*) que apresenta os resultados num formato visualmente premium e responsivo.

---

## 🌟 Funcionalidades Principais

- **Automação de Extração**: Scripts em Python buscam as 100 postagens mais recentes de tópicos específicos diretamente da API JSON do Reddit.
- **Filtro Temporal**: Mantém exclusivamente posts criados nos últimos 7 dias.
- **Algoritmo de Engajamento**: Rankeia os posts utilizando uma pontuação consolidada de `Score (Upvotes) + Comentários`, trazendo à tona o que realmente gerou discussão.
- **Visualização Premium (Web App)**: Uma interface limpa desenvolvida com HTML, CSS (Vanilla) e JavaScript, empregando princípios de UI modernos (Glassmorphism, High-contrast Neon Accents e fontes sem-serifa).
- **Sistema Centralizado de Logs**: Todos os processos e extrações são meticulosamente registrados para auditorias futuras.

---

## 🛠️ Tecnologias Utilizadas

- **Backend / Automação**: `Python 3`, `Requests`
- **Frontend / Visualização**: `HTML5`, `CSS3` (Vanilla), `JavaScript` (ES6)
- **Design System**: Estética *Dark Mode* personalizada com acentos `#ffd900` (Amarelo Neon).
- **Persistência de Dados**: JSON local estático (`.tmp/`).

---

## ⚙️ Como Executar o Projeto

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/renato123b/reddit-dashboard-automation.git
   cd reddit-dashboard-automation
   ```

2. **Gere os dados mais recentes**:
   Execute o script Python informando quais subreddits você deseja rastrear:
   ```bash
   python execution/fetch_reddit_posts.py n8n automation
   ```
   *(Isso criará o banco de dados temporário em `.tmp/reddit_top_5.json` e os logs da operação em `logs/automation.log`)*

3. **Inicie o Servidor do Dashboard**:
   A interface gráfica exige um servidor estático para realizar as requisições (devido às políticas de CORS dos navegadores):
   ```bash
   python -m http.server 8000
   ```

4. **Acesse a Aplicação**:
   Abra seu navegador favorito e acesse: [http://localhost:8000/app/](http://localhost:8000/app/)

---

## 📁 Estrutura de Diretórios

```text
/
├── app/                  # Web App Frontend (HTML/CSS/JS)
├── directives/           # Arquivos de SOP e definição de regras
├── execution/            # Scripts principais em Python
│   ├── utils/            # Módulos compartilhados (ex: logger.py)
│   └── fetch_posts.py    # Motor principal
├── logs/                 # (GitIgnored) Arquivos de registro
└── .tmp/                 # (GitIgnored) Banco de dados estático em JSON
```

---

> Desenvolvido com foco em arquitetura de 3 camadas (Diretrizes, Orquestração e Execução) para máxima confiabilidade e manutenção.
