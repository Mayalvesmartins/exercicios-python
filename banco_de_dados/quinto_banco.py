import sqlite3

# Conectar ao banco existente (ou criar um novo)
conexao = sqlite3.connect("banco_fic.db")
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
clientes = [
    ("Ana Silva", "ana@email.com", "(62)99999-1111", "Goiânia"),
    ("Carlos Oliveira", "carlos@email.com", "(21)88888-2222", "Rio de Janeiro"),
    ("Mariana Costa", "mariana@email.com", "(31)97777-3333", "Belo Horizonte"),
    ("Pedro Santos", "pedro@email.com", "(41)96666-4444", "Aparecida de Goiânia"),
    ("Fernanda Lima", "fernanda@email.com", "(64)95555-5555", "Rio Verde"),
    ("Paulo Abreu", "pauloabreu@email.com", "(62)98555-2333", "Goiânia"),
    ("João Carlos", "joaocarlos@email.com", "(62)96666-4444", "Goiânia")
]

cursor.execute("DELETE FROM clientes;")  # limpa a tabela antes de inserir
cursor.executemany("""
INSERT INTO clientes (nome, email, telefone, cidade)
VALUES (?, ?, ?, ?);
""", clientes)

conexao.commit()

# ==============================
# CONSULTA COM FILTRO (WHERE)
# ==============================
cidade_desejada = "Goiânia"
cursor.execute("SELECT id, nome, email, telefone, cidade FROM clientes WHERE cidade = ?;", (cidade_desejada,))
resultados = cursor.fetchall()

# Cabeçalho formatado
print(f"{'Nº':<3} {'ID':<3} {'Nome':<18} {'Email':<25} {'Telefone':<17} {'Cidade'}")
print("-" * 90)
print(f"Clientes da cidade de {cidade_desejada}:")

# Exibir os resultados
for i, (id, nome, email, telefone, cidade) in enumerate(resultados, start=1):
    print(f"{i:<3} {id:<3} {nome:<18} {email:<25} {telefone:<17} {cidade}")

# Fechar a conexão
conexao.close()


