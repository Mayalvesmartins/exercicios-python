print('calculo das raizes da equacao de 2 grau: ax² + bx + c = 0')
a = float(input('informe o valor de a: '))
b = float(input('informe o valor de b: '))
c = float(input('informe o valor de c: '))
delta = b**2 - 4*a*c
if delta < 0:
    print('A equacao nao possui raizes reias. ')
elif delta == 0:
    raiz = -b / (2*a)
    print(f'A equacao possui uma raiz real: {raiz}')
else:
    raiz1 = (-b + (delta ** 0.5)) / (2*a)
    raiz2 = (-b - (delta ** 0.5)) / (2*a)
    print(f'As raizes da equacao sao: `{raiz1} e {raiz2}')
