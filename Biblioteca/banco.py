import sqlite3

def conection():
    conexao = sqlite3.connect("BibliotecaCoraCoralina.db")
    cursor = conexao.cursor()

    try:
        # Tabela livros
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS livros (
                            isbn VARCHAR(20) PRIMARY KEY,
                            titulo VARCHAR(255) NOT NULL,
                            subtitulo VARCHAR(255),
                            editora VARCHAR(255),
                            ano_publicacao DATE,
                            idioma VARCHAR(50) NOT NULL
                        );
        ''')

        # Tabela autores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nascimento DATE,
                data_falecimento DATE,
                nacionalidade TEXT
            )
        ''')

        # Tabela usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                data_nascimento DATE,
                email TEXT NOT NULL,
                celular TEXT NOT NULL
            )
        ''')

        # Tabela autores_livros
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS autores_livros (
                isbn TEXT,
                id_autor INTEGER,
                PRIMARY KEY (isbn, id_autor),
                FOREIGN KEY (isbn) REFERENCES livros(isbn),
                FOREIGN KEY (id_autor) REFERENCES autores(id)
            )
        ''')

        # Tabela emprestimos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emprestimos (
                id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn TEXT NOT NULL,
                cpf TEXT NOT NULL,
                data_emprestimo DATE NOT NULL DEFAULT CURRENT_DATE,
                data_devolucao DATE,
                FOREIGN KEY (isbn) REFERENCES livros(isbn),
                FOREIGN KEY (cpf) REFERENCES usuarios(cpf)
            )
        ''')

        conexao.commit()
        print("Tabelas criadas com sucesso.")

    except sqlite3.Error as erro:
        print(f"Erro ao criar tabelas: {erro}")

    return conexao

