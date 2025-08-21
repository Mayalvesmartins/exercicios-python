# # Criando um dicionário
# estoque = {
#     "maçã": 10,
#     "banana": 5,
#     "laranja": 8
# }

# # Acessando valores pela chave
# estoque["maçã"] # 10

# # Adicionando um item
# estoque["pera"] = 12

# # Alterando valor
# estoque["banana"] = 7

# # Removendo item
# del estoque["laranja"]

# # Percorrendo dicionário
# # for fruta, qtd in estoque.items():
# #     print(fruta, qtd)


# Criando conjuntos
frutas = {"maçã", "banana", "laranja", "maçã"}  

print(frutas)   # {'maçã', 'banana', 'laranja'} → repetidos somem

# Adicionando elementos
frutas.add("pera")

# Removendo elementos
frutas.remove("banana")

# Operações de conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # União → {1, 2, 3, 4, 5, 6}
print(a & b)  # Interseção → {3, 4}
print(a - b)  # Diferença → {1, 2}
print(a ^ b)  # Diferença simétrica → {1, 2, 5, 6}
