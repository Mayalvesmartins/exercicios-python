import sqlite3
def conection():
    #Criação da conexão com o banco
    conexao = sqlite3.connect("alunos.db")

    #Criação do cursor
    cursor = conexao.cursor()

    # Criar o banco

    try:
        cursor.execute ('''CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT, idade INTEGER)''')
        conexao.commit()
    except sqlite3.Error as erro:
        print(f"Erro no banco: {erro}")
    return conexao