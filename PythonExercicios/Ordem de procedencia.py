n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma e {}, o produto e {} e a divisao e {:.3f}'.format(s, m, d), end=' ')
print('divisao inteira {} e potencia {}'. format(di, e))