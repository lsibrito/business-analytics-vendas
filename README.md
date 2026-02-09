<p align="center">
  <img src="./logo.png" width="120">
</p>

  <h1>📊 Análise de Vendas com KPIs</h1>
</div>

---

# Análise de Vendas e KPIs com Python e SQL

## 🎯 O Objetivo
Criei este projeto para simular um dia a dia real de um analista de dados. A ideia não era apenas gerar gráficos, mas construir todo o fluxo de dados "do zero": começando pela estruturação de um banco de dados (SQLite), passando pela ingestão dos dados e finalizando com a extração de inteligência de negócio (Business Analytics).

Meu foco aqui foi responder a perguntas de negócio como: *"Qual região está performando melhor?"* e *"Qual é o nosso ticket médio real?"*.

## 🛠 O que eu usei (Tech Stack)
Para simular um ambiente corporativo sem a complexidade de servidores na nuvem, escolhi:
* **Python:** Para orquestrar todo o processo.
* **SQLite + SQL:** Queria exercitar a criação de tabelas e consultas manuais (`SELECT`, `GROUP BY`), fugindo um pouco da dependência total do Pandas para tudo.
* **Pandas:** Para manipulação avançada dos DataFrames e cálculos estatísticos.
* **Matplotlib:** Para traduzir os números em visualização gráfica simples e direta.

## 🚀 Como o projeto funciona
O script `main.py` executa o pipeline completo em 5 etapas:
1.  **Conexão e Setup:** Cria automaticamente o banco `vendas.db` se ele não existir.
2.  **Ingestão:** Simula a entrada de novas vendas no sistema.
3.  **Processamento:** Usa SQL para agregar os dados brutos diretamente na fonte.
4.  **Cálculo de KPIs:** Gera métricas de Faturamento Total e Ticket Médio.
5.  **Dataviz:** Exporta gráficos que mostram a performance por Região e Categoria.

## 📊 Exemplos de Insights
Ao rodar o projeto com os dados de amostra, conseguimos identificar padrões claros, como a predominância de faturamento na categoria de **Eletrônicos** em comparação a **Móveis**, o que sugeriria, num cenário real, um foco maior de estoque para essa categoria.

## 🔜 Próximos Passos
Para evoluir este portfólio, estou trabalhando nas seguintes melhorias:
- [ ] Implementar um modelo preditivo com **Scikit-Learn** para prever o faturamento do próximo mês (Regressão Linear).
- [ ] Criar um dashboard interativo (Streamlit ou Power BI).
- [ ] Adicionar tratamento de datas mais robusto para análise de sazonalidade.

---
*Desenvolvido por Leonardo Brito - São Carlos, SP*


