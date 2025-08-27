# print('lista de leituras')
# print(input('Digite o nome do livro: '))
# nome = ''
# lista_de_leituras = []
# while nome != ('fim'):
#     nome = input()
#     if nome != ('fim'):
#         lista_de_leituras.append(nome)
# print(lista_de_leituras)



print("=== Lista de Leituras ===")
lista_de_leituras = []

while True:
    nome = input("Digite o nome do livro (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':  # para aceitar 'FIM', 'Fim' etc.
        break
    lista_de_leituras.append(nome)

# Ordenar alfabeticamente
lista_de_leituras.sort()

# Exibir de forma organizada
print("\nLivros lidos no ano:")
print("-------------------")
for i, livro in enumerate(lista_de_leituras, 1):
    print(f"{i}. {livro}")


# print ('=== Lista de leituras ===')

# livro = ['O conde de monte cristo',
# 'O morro dos ventos uivantes',
# 'A divina comedia', 
# 'o senhor dos aneis', 
# 'uma mulher na janela', 
# 'a garota no gelo', 
# 'vingadores', 
# 'a menina feita de espinhos', 
# 'a paciente silenciosa', 
# 'fallen' , 'diarios de um vampiro', 
# 'corte de neve e rosas', 
# 'a rainha vermelha', 
# 'a seleção', 
# 'o princpe', 
# 'o pequeno principe', 
# 'o hobbit', 
# 'a culpa e das estrelas', 
# 'o lar da srta peregrine para criancas peculiares', 
# 'a casa das orquideas']
# print (livro)
