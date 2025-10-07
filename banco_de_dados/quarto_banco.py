import sqlite3

# ==============================
# CONEXÃO COM O BANCO DE DADOS
# ==============================
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# ==============================
# CRIAÇÃO DA TABELA CLIENTES
# ==============================
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS clientes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     email TEXT,
#     telefone TEXT,
#     cidade TEXT
# );
# """)

# ==============================
# INSERÇÃO DE DADOS FICTÍCIOS
# ==============================
cursor.execute("DELETE FROM clientes;")

clientes = [
    ("Ana Silva", "Goiânia"),
    ("Carlos Oliveira", "Rio de Janeiro"),
    ("Mariana Costa", "Belo Horizonte"),
    ("Pedro Santos","Aparecida de Goiânia"),
    ("Fernanda Lima", "Rio Verde"),
    ("Paulo Abreu","Goiânia"),
    ("João Carlos", "Goiânia")
]

cursor.executemany("""
INSERT INTO clientes (nome, cidade)
VALUES (?, ?);
""", clientes)

conexao.commit()
print(" Banco de dados 'banco.db' criado com sucesso com a tabela 'clientes'!")

# ==============================
# CONSULTAR E MOSTRAR RESULTADOS
# ==============================
cursor.execute("SELECT nome, cidade FROM clientes;")
resultados = cursor.fetchall()

print("\n Lista de clientes cadastrados:\n")

# Cabeçalho formatado
print(f"{'Nº':<3} {'ID':<3} {'Nome':<18} {'Cidade'}")
print("-" * 80)

# Mostrar dados com índice
for i, (nome, cidade) in enumerate(resultados, start=1):
    print(f"{i:<3} {nome:<18} {cidade}")

# ==============================
# ENCERRAR CONEXÃO
# ==============================
conexao.close()
