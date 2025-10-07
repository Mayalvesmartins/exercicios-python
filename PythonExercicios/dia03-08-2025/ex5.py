valor = float(input('Valor da compra: '))
if (valor <= 100):
    percentualDesconto = 5/100
if (valor > 101 and valor < 500):
    percentualDesconto = 10/100
if (valor >= 500):
    percentualDesconto = 15/100
valorComDesconto = valor - valor * percentualDesconto
print(f'valor da compra e {valor} com desconto {valorComDesconto}')