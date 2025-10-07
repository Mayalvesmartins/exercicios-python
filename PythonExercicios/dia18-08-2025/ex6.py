cores = ("vermelho", "verde", "azul", "amarelo", "roxo")
if 'azul' in cores:
    print('azul esta na tupla! ')
else:
    print('azul nao esta na tupla! ')
print(f'primeira cor: {cores[0]}')
print(f'ultima cor: {cores[-1]}')
try:
    cores[0] = 'preto'
except TypeError as e:
    print(f'Erro: {e} ')