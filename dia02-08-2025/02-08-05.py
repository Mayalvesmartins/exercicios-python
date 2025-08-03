nome = input('Nome do funcionario: ')
salario = float(input('Salario: '))
vendas = float(input('venda no mes: '))
if vendas >= 3000:
    salarioBonus = salario + (20/100) * salario 
if vendas < 3000:
    salarioBonus = 0
print(f'{nome}, seu salario total com bonus e R${salarioBonus}')
