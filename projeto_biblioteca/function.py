from datetime import datetime

def valida_data(data_publicacao):
    try:
        data_validada = datetime.strptime(data_publicacao, "%d-%m-%Y")
        data_formatada = data_validada.strftime("%Y-%m-%d")
        return data_formatada
    except ValueError:
        print("❌ Data inválida. Tente novamente no formato DD-MM-AAAA.")
        return None

# Funções de banco
def cadastrar_livros(conexao, livro):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO livros (isbn, titulo, subtitulo, editora, ano_publicacao, idioma) VALUES (?, ?, ?, ?, ?, ?)", livro.para_tupla())
    conexao.commit()
    print("✅ Livro cadastrado!")
    return True


def listar_livros(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    return cursor.fetchall()

