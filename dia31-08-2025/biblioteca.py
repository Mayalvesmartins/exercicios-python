livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "categoria": "Romance" , "ano": "1899"},
    {"titulo": "o principe cruel" , "autor": "Kiera Cass", "categoria": "Romance" , "ano": "2013"},
    {"titulo": "Fallen" , "autor": "Lauren Kate", "categoria": "Romance" , "ano": "2009"},
    {"titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "categoria": "Fantasia" , "ano": "1997"},
    {"titulo": "1984", "autor": "George Orwell", "categoria": "Distopia" , "ano": "1949"},
    {"titulo": "A Revolução dos Bichos", "autor": "George Orwell", "categoria": "Sátira" , "ano": "1945"},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "categoria": "Infantil" , "ano": "1943"},
    {"titulo": "A Menina que Roubava Livros", "autor": "Markus Zusak", "categoria": "Drama" , "ano": "2005"},
    {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "categoria": "Romance" , "ano": "1813"},
    {"titulo": "O Senhor dos Anéis: A Sociedade do Anel", "autor": "J.R.R. Tolkien", "categoria": "Fantasia" , "ano": "1954"},
    {"titulo": "O Alquimista", "autor": "Paulo Coelho", "categoria": "Ficção" , "ano": "1988"},
    {"titulo": "crepusculo" , "autor": "Stephenie Meyer", "categoria": "Romance" , "ano": "2005"},
    {"titulo": "O Código Da Vinci", "autor": "Dan Brown", "categoria": "Suspense" , "ano": "2003"},
    {"titulo": "A Culpa é das Estrelas", "autor": "John Green", "categoria": "Romance" , "ano": "2012"},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "categoria": "Fantasia" , "ano": "1937"},
    {"titulo": "O Diário de Anne Frank", "autor": "Anne Frank", "categoria": "Biografia" , "ano": "1947"},
    {"titulo": "A Cabana", "autor": "William P. Young", "categoria": "Ficção" , "ano": "2007"},
    {"titulo": "O Morro dos Ventos Uivantes", "autor": "Emily Brontë", "categoria": "Romance Gótico" , "ano": "1847"},
    {"titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams", "categoria": "Ficção Científica" , "ano": "1979"},
    {"titulo": "o que esta la fora" , "autor": "kate alice marsh" , "categoria": "Ficção Científica" , "ano": "2023"},
]

nome=input("Digite seu nome: ")

print(f"Olá {nome}, seja Bem-vindo à Biblioteca MayFran!")
print("Você pode escolher uma das opções abaixo:")

def imprime_menu():
    print("\n=== Biblioteca MayFran ===")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro pelo título")
    print("4 - Ver categorias")
    print("5 - Ver se o livro está disponível")
    print("6 - Sair")

def adicionar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")
    ano = input("Ano de publicação: ")

    livro = {"titulo": titulo, "autor": autor, "categoria": categoria , "ano": ano}
    livros.append(livro)
    print("Livro cadastrado!")


def listar_livros():
    if not livros:
            print("Nenhum livro cadastrado.")
    else:
    
        categorias = {}
        for l in livros:
            cat = l["categoria"]
            if cat not in categorias:
                categorias[cat] = []
            categorias[cat].append(l)

        for categoria, lista in categorias.items():
            print(f"\n=== {categoria} ===")
            for l in lista:
                print(f"- {l['titulo']} ({l['autor']}, {l['ano']})")

def buscar_livro():
    termo = input("Digite parte do título: ").lower()
    achou = False
    for l in livros:
        if termo in l["titulo"].lower():
            print(f"{l['titulo']} - {l['autor']} ({l['categoria']}, {l['ano']})")
            achou = True
    if not achou:
        print("Livro não encontrado.")

def listar_categorias():
    categorias = {l["categoria"] for l in livros}
    if categorias:
        print("Categorias disponíveis:")
        for c in categorias:
            print("-", c)
    else:
        print("Nenhuma categoria cadastrada.")

def verificar_disponibilidade():
    titulo = input("Digite o título do livro: ").lower()
    disponivel = any(titulo == l["titulo"].lower() for l in livros)
    if disponivel:
        print("O livro está disponível.")
    else:
        print("O livro não está disponível.")

while True:
    imprime_menu()

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1": adicionar_livro()
        case "2": listar_livros()
        case "3": buscar_livro()
        case "4": listar_categorias()
        case "5": verificar_disponibilidade()
        case "6":
            print("Obrigado por usar a Biblioteca MayFran. Até logo!")
            break
        case _:
            print("Opção inválida, tente novamente!")
