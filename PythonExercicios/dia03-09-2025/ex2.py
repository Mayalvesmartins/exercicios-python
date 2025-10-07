
# def calcular_media(n1, n2, n3):
#     media = (n1 + n2 + n3) / 3
#     return media

# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# nota3 = float(input('Digite a terceira nota: '))

# resultado = calcular_media (nota1 , nota2 , nota3)
# print(f'A soma das medias e {resultado:.2f}')


def cabecalho():
    print("\n------------------- Relatório Final -------------------")
    print(f"{'nome':<15} {'n1':<6} {'n2':<6} {'n3':<6} {'media':<8} {'situacao'}")
    print("-" * 55)

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
    except ValueError:
        print("Por favor digite somente numeros validos para as notas.")
        continue

    media = calcular_media(nota1, nota2, nota3)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "n1": nota1,
        "n2": nota2,
        "n3": nota3,
        "media": round(media, 2),
        "situacao": situacao
    }

    alunos.append(aluno)

if alunos:
    cabecalho()
    for aluno in alunos:
        print(f"{aluno['nome']:<15} {aluno['n1']:<6.1f} {aluno['n2']:<6.1f} {aluno['n3']:<6.1f} {aluno['media']:<8.2f} {aluno['situacao']}")

else:
    print("\nNenhum aluno foi cadastrado.")
