import sqlite3

# conectar
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# # criar tabela (só se não existir ainda)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS pessoas (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER NOT NULL
# )
# """)

# inserir um registro
# cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ("Samarah", 22))
cursor.execute(" SELECT * FROM pessoas WHERE idade < 10")
resultados = cursor.fetchall()


print("ID | Nome     | Idade")
print("-" * 25)
for pessoa in resultados:
    id_, nome, idade = pessoa
    print(f"{id_:<2} | {nome:<8} | {idade}")


# salvar mudanças
conexao.commit()

# fechar
conexao.close()

