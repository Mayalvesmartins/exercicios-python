def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

resultado = calcular_media (nota1 , nota2 , nota3)
print(f'A soma das medias e {resultado:.2f}')


