idade = int(input('digite sua idade: '))
nome = input('digite seu nome: ')
if idade >=18:
    informacao = ('Voce e maior de idade.')
if idade < 18:
    informacao = ('Voce e menor de idade')
print('seu nome e', nome , 'e' , informacao )