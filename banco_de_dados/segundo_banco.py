import sqlite3
#importando a biblioteca

banco = sqlite3.connect('segundo_banco.db')
#criando o primeiro banco de dados

cursor = banco.cursor()
#objeto do banco para podermos operar dentro do banco

# cursor.execute("CREATE TABLE texto (nome text, idade integer, curso text)")


cursor.execute("INSERT INTO texto (nome, idade, curso) VALUES (?,?,?)", ("Ana", 20, "ADS"))
texto = [
    ('João', 22, "engenharia"),
    ('Maria', 21, "portugues"),
    ('Pedro', 23, "odontologia"),
    ('Lucas', 24, "quimica")
]

cursor.executemany("INSERT INTO texto (nome, idade, curso) VALUES (?,?,?)", texto)
#inserindo dados na tabela(deve comentar a criação da tabela)

banco.commit()
#comando para salvar as inserções

cursor.execute("SELECT * FROM texto")
print(cursor.fetchall())
#visualizar os dados