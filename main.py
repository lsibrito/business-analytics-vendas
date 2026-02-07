import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# 1. Conectar ao banco
# ==========================
conn = sqlite3.connect("vendas.db")
cursor = conn.cursor()

# ==========================
# 2. Criar tabela
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    produto TEXT,
    categoria TEXT,
    valor REAL,
    quantidade INTEGER,
    regiao TEXT
)
""")

# ==========================
# 3. Inserir dados
# ==========================
dados = [
    ("2025-01-01", "Notebook", "Eletronicos", 3500, 1, "Sudeste"),
    ("2025-01-02", "Mouse", "Eletronicos", 80, 3, "Sul"),
    ("2025-01-03", "Cadeira", "Moveis", 900, 2, "Sudeste"),
    ("2025-01-05", "Teclado", "Eletronicos", 150, 4, "Nordeste"),
    ("2025-02-01", "Notebook", "Eletronicos", 3500, 1, "Sul"),
    ("2025-02-10", "Mesa", "Moveis", 1200, 2, "Sudeste")
]

cursor.executemany("""
INSERT INTO vendas (data, produto, categoria, valor, quantidade, regiao)
VALUES (?, ?, ?, ?, ?, ?)
""", dados)

conn.commit()

# ==========================
# 4. KPI Geral (SQL)
# ==========================
kpi_query = """
SELECT 
    SUM(valor * quantidade) AS faturamento_total,
    AVG(valor * quantidade) AS ticket_medio,
    SUM(quantidade) AS quantidade_total
FROM vendas
"""

kpis = pd.read_sql_query(kpi_query, conn)
print("===== KPIs Gerais =====")
print(kpis)

# ==========================
# 5. Faturamento por Categoria (SQL)
# ==========================
categoria_query = """
SELECT 
    categoria,
    SUM(valor * quantidade) AS faturamento_total
FROM vendas
GROUP BY categoria
"""

df_categoria = pd.read_sql_query(categoria_query, conn)

print("\n===== Faturamento por Categoria =====")
print(df_categoria)

# ==========================
# 6. Faturamento por Região (SQL)
# ==========================
regiao_query = """
SELECT 
    regiao,
    SUM(valor * quantidade) AS faturamento_total
FROM vendas
GROUP BY regiao
"""

df_regiao = pd.read_sql_query(regiao_query, conn)

print("\n===== Faturamento por Região =====")
print(df_regiao)

# ==========================
# 7. Visualização
# ==========================
plt.figure()
plt.bar(df_categoria["categoria"], df_categoria["faturamento_total"])
plt.title("Faturamento por Categoria")
plt.ylabel("Faturamento")
plt.show()

conn.close()