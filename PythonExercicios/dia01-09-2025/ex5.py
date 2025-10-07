def calcular_situacao(nome, nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'
    return f'{nome} esta {situacao} com media {media:.2f}'
resultado = calcular_situacao('Mayara', 6, 7, 8)
print(resultado)

