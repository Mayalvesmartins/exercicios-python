livros = [
    {"titulo": "Fallen" , "autor": "Lauren Kate", "categoria": "Romance" , "ano": "2009"},
    {"titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "categoria": "Fantasia" , "ano": "1997"}
]

print('Bem vindo a biblioteca.')

while True:
    print('1 - Livros disponiveis')
    print('2 - sair')
    print('3 - cadastrar livro')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        for i, livro in enumerate (livros):
            print(i+1, '-' , livro['titulo'],  livro['autor'], '(' ,livro['categoria'], livro['ano'], ')')
        print(f'\n=============================\n')

    elif opcao == '3':
        titulo = input('titulo: ')
        autor = input('autor: ')
        categoria = input('categoria: ')
        ano = input('ano: ')
        livros.append({"titulo": titulo , "autor": autor, "categoria": categoria, "ano": ano})
        print('Livro cadastrado.')
    

    else:
        print('obrigado por usar a biblioteca.')
        break
    


