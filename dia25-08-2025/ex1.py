# num = int(input("Digite um número: "))
# if num % 2 == 0:
#     print("Par")
# else:
#     print("Ímpar")


# nota1 = float(input("Nota 1: "))
# nota2 = float(input("Nota 2: "))
# media = (nota1 + nota2) / 2

# if media >= 7:
#     print(f"O aluno tem média {media} e por isso ele foi Aprovado")
# else:
#     print(f"O aluno tem média {media} e por isso ele foi Reprovado")


# senha_correta = "324578"
# senha = input("Digite a senha: ")
# while senha != senha_correta:
#     print("Senha incorreta")
#     senha = input("Digite a senha: ")
# print("Senha correta! Acesso liberado")



# nome = input('Digite o nome do seu pet: ')
# idade = int(input('Digite a idade do seu pet: '))
# tipo = input('Digite o tipo de seu pet (cachorro, gato, peixe): ').lower()

# if tipo == 'cachorro':
#     raca = input('Digite a raça do cachorro: ').lower()
#     if raca == 'poodle':
#         print(f'{nome} é um cachorro da raça {raca} e tem {idade} anos')
#     elif raca == 'labrador':
#         print(f'{nome} é um cachorro da raça {raca} e tem {idade} anos')
#     else:
#         print(f'{nome} é um cachorro de raça {raca} e tem {idade} anos')

# elif tipo == 'gato':
#     cor = input('Digite a cor do gato: ').lower()
#     if cor == 'preto':
#         print(f'{nome} é um gato da cor {cor} e tem {idade} anos')
#     elif cor == 'branco':
#         print(f'{nome} é um gato da cor {cor} e tem {idade} anos')
#     else:
#         print(f'{nome} é um gato da cor {cor} e tem {idade} anos')

# elif tipo == 'peixe':
#     agua = input('Digite o tipo de água do peixe (doce, salgada): ').lower()
#     if agua == 'doce':
#         print(f'{nome} é um peixe de água doce e tem {idade} anos')
#     elif agua == 'salgada':
#         print(f'{nome} é um peixe de água salgada e tem {idade} anos')
#     else:
#         print(f'{nome} é um peixe de água desconhecida e tem {idade} anos')

# else:
#     print('Tipo de pet desconhecido')



nome = input('Digite o nome do seu pet: ')
idade = int(input('Digite a idade do seu pet: '))
tipo = input('Digite o tipo de seu pet (cachorro, gato, peixe): ').lower()

if tipo == "cachorro":
    raca = input("Digite a raça do cachorro: ").lower()
    raças_validas = {
        "poodle": f"{nome} é um cachorro da raça poodle e tem {idade} anos",
        "labrador": f"{nome} é um cachorro da raça labrador e tem {idade} anos"
    }
    print(raças_validas.get(raca, f"{nome} é um cachorro da raça {raca} e tem {idade} anos"))

elif tipo == "gato":
    cor = input("Digite a cor do gato: ").lower()
    cores_validas = {
        "preto": f"{nome} é um gato da cor preta e tem {idade} anos",
        "branco": f"{nome} é um gato da cor branca e tem {idade} anos"
    }
    print(cores_validas.get(cor, f"{nome} é um gato da cor {cor} e tem {idade} anos"))

elif tipo == "peixe":
    agua = input("Digite o tipo de água do peixe (doce, salgada): ").lower()
    aguas_validas = {
        "doce": f"{nome} é um peixe de água doce e tem {idade} anos",
        "salgada": f"{nome} é um peixe de água salgada e tem {idade} anos"
    }
    print(aguas_validas.get(agua, f"{nome} é um peixe de água desconhecida e tem {idade} anos"))

else:
    print("Tipo de pet desconhecido")
