idade = int(input('Qual a idade: '))
if (idade <= 12):
    categoria = 'criança'
if (idade >= 13 and idade <= 17 ):
    categoria = 'adolescente'
if (idade >= 18 and idade <= 59):
    categoria = 'adulto'
if (idade >= 60):
    categoria = 'idoso'
print(f'a sua idade e {idade} voce e {categoria}')