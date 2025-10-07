# Classe livro
class Livro:
    def __init__(self, titulo, subtitulo, editora, data_publicacao, idioma, CodISBN):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.editora = editora
        self.data_publicacao = data_publicacao
        self.idioma = idioma
        self.CodISBN = CodISBN

    def exibir_dados(self):
        return f"Título: {self.titulo}, Subtítulo: {self.subtitulo}, Editora: {self.editora}, Data de Publicação: {self.data_publicacao}, Idioma: {self.idioma}, ISBN: {self.CodISBN}"


    def para_tupla(self):
        return (self.CodISBN, self.titulo, self.subtitulo, self.editora, self.data_publicacao, self.idioma)



# Classe Autor
class Autor:
    def __init__(self, nome, data_nascimento, data_falecimento, nacionalidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.data_falecimento = data_falecimento
        self.nacionalidade = nacionalidade

    def exibir_dados(self):
        return f"Nome: {self.nome}, Nascimento: {self.data_nascimento}, Falecimento: {self.data_falecimento}, Nacionalidade: {self.nacionalidade}"

    def para_tupla(self):
        return (self.nome, self.data_nascimento, self.data_falecimento, self.nacionalidade)


# Classe Usuario
class Usuario:
    def __init__(self, cpf, nome, data_nascimento, email, celular):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.email = email
        self.celular = celular

    def exibir_dados(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Nascimento: {self.data_nascimento}, Email: {self.email}, Celular: {self.celular}"

    def para_tupla(self):
        return (self.cpf, self.nome, self.data_nascimento, self.email, self.celular)
