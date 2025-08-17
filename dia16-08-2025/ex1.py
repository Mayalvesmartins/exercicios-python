# x = int(input("Digite um numero: "))
# y = int(input("Digite o segundo numero: "))
# if(x > y):
#     print(f"O {x} é maior que o {y}")
# else:
#     print(f"O {y} é maior que o {x}")

# numero = int(input("Digite um número: "))
# for i in range(5,15):
#     print(f'{numero} x {i + 1} = {numero * (i + 1)}')

numero = int(input("Digite um numero: "))
i = 1
while i <= 10:
    print(f'{numero} x {i} = {numero * i}')
    i += 1

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1
# print("Fim")

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# media = (nota1 + nota2 + nota3) / 3
# print(f"Media: {media}")
# if(media >= 7):
#     print(f"Sua média foi {media:.2f}  e você foi Aprovado!")
# else:
#     print(f"Sua média foi {media:.2f}  e você foi Reprovado!")


# temperatura = float(input("Digite uma temperatura em Celsius: "))
# temperaturaEmFahrenheit = temperatura * (9 / 5) + 32
# print(f'A temperatura em Fahrenheit é: {temperaturaEmFahrenheit:.1f} ºF')


# idade = int(input('Digite sua idade: '))
# if idade >= 18:
#     print('A pessoa e maior de idade. ')
# else:
#     print('A pessoa e menor de idade. ')


# palavra = input('Digite a palavra: ')
# contagem = 0
# for i in palavra:
#     contagem += 1
#     print(f'{i} - {contagem} ')
# print(f'são {contagem} letras. ')


# palavra = input('Digite a palavra: ')
# contagem = 0
# for i in palavra:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#          contagem += 1
#     print(f'{i} - {contagem} ')
# print(f'são {contagem} vogais. ')


# import random
# numero = random.randint(1 , 10)
# usuario = int(input('De o seu palpite: '))
# if numero == usuario:
#     print('voce acertou. ')
# else:
#     print('voce errou. ')
# print(f'o numero gerado pelo computador foi {numero}, o seu numero foi {usuario}. ')