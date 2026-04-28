# Extrair Top 5 Posts do Reddit

**Objetivo:** Buscar os 100 posts mais recentes de subreddits específicos, filtrar os que foram criados nos últimos 7 dias, e extrair os 5 com maior engajamento (score + comentários).

**Inputs:**
- Lista de subreddits (ex: `n8n`, `automation`).

**Execução (Ferramenta):**
O script responsável por esta extração é `execution/fetch_reddit_posts.py`.
Você deve chamá-lo passando os nomes dos subreddits como argumentos separados por espaço.

*Exemplo:*
```bash
python execution/fetch_reddit_posts.py n8n automation
```

**Outputs Esperados:**
- **.tmp/reddit_raw_data.json**: Arquivo com os dados completos obtidos da API (intermediário).
- **.tmp/reddit_top_5_summary.md**: Arquivo formatado contendo os top 5 posts de cada subreddit solicitado.

**Edge Cases & Tratamento de Erros:**
- *Rate Limits*: O script usa um User-Agent customizado para acessar o JSON público. Se começar a receber erros `429 Too Many Requests`, notifique o usuário para que seja configurada a autenticação OAuth do Reddit no arquivo `.env`.
- *Subreddit Inexistente*: O script deve avisar caso um subreddit retorne 404.
- *Menos de 5 posts na semana*: O script deve retornar o máximo disponível se não houver 5 posts recentes.
