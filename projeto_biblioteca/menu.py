from function import *
from banco import *
from classes import *


def menu():
    while True:
        print("\n+----------------------+")
        print("|     === MENU ===     |")
        print("+----------------------+")
        print("| 1 - Cadastrar Livro  |")
        print("| 2 - Cadastrar Usuário    |")
        print("| 3 - Alterar Livro     |")
        print("| 4 - Alterar Usuário    |")
        print("| 5 - Deletar Livro    |")
        print("| 6 - Deletar Usuário    |")
        print("| 7 - Cadastrar empréstimo    |")
        print("| 8 - Finalizar empréstimo    |")
        print("| 9 - Listar livros    |")
        print("| 0 - Sair             |")
        print("+----------------------+")

        opcao = input("| Escolha uma opção:   |")

        if opcao == "1":  # Cadastrar Livro
            titulo = input("Título: ")
            subtitulo = input("Subtítulo: ")  # texto
            editora = input("Editora: ")       # texto

            # Validação da data
            while True:
                data_publicacao = input("Digite a data de publicação (DD-MM-AAAA): ")
                data_publicacao_valida = valida_data(data_publicacao)
                if data_publicacao_valida:
                    break

            idioma = input("Idioma: ")
            CodISBN = input("ISBN: ")

            livro = Livro(titulo, subtitulo, editora, data_publicacao_valida, idioma, CodISBN)

            cadastrar_livros(conection(), livro)

        elif opcao == "9": #Listar livros
            livro = listar_livros(conection())
            for a in livro:
                print(a)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")
