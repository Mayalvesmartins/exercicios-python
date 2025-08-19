# nomes = [ ]
# for i in range(3):
#     nome=input('Digite um nome: ')
#     nomes.append(nome)
# print('\nlista de nomes: ')
# print(nomes)
# print('\nNomes na lista: ')
# for nome in nomes:
#     print(nome)



nomes=[ ]
idades=[ ]
for i in range(3):
    nome=input('Digite um nome: ')
    idade=int(input('Digite uma idade: '))
    nomes.append(nome)
    idades.append(idade)
print('\nlista de nomes: ')
print(nomes,idades)
print('\nNomes na lista: ')
for nome in nomes:
    print(nome)

for idade in idades:
    print(idade)