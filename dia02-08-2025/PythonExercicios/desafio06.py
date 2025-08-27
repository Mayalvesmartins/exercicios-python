real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 5.59
print('com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))