import random

print("--- Jogo do Número Secreto ---")

while True:
    numero_secreto = random.randint(1, 100)
    tentativas = 5

    print("O computador escolheu um número secreto entre 1 e 100.")
    print(f"Você tem {tentativas} tentativas para acertar.")

    for i in range(tentativas):
        try:
            palpite = int(input(f"Tentativa {i + 1}/{tentativas}. Digite seu palpite: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número secreto!")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior que o seu palpite.")
        else:
            print("O número secreto é menor que o seu palpite.")
    else:
        print("Suas tentativas acabaram.")
        print(f"O número secreto era: {numero_secreto}")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        break

print("Obrigado por jogar!")

# Explicação linha por linha

# import random – importa o módulo random, que dá acesso a funções de números aleatórios.

# linha em branco – só organiza visualmente o código.

# print("--- Jogo do Número Secreto ---") – mostra o título do jogo na tela.

# linha em branco – separação visual.

# while True: – inicia um laço infinito; ele só termina quando fizermos break. Cada volta representa uma “partida”.

# numero_secreto = random.randint(1, 100) – sorteia um inteiro entre 1 e 100 (inclusive) para ser o número secreto desta partida.

# tentativas = 5 – define quantas chances o jogador terá.

# linha em branco – separação visual.

# mensagem – informa o intervalo do número secreto.

# mensagem com f-string – informa quantas tentativas o jogador terá (usa o valor de tentativas).

# linha em branco – separação visual.

# for i in range(tentativas): – laço que vai de 0 a tentativas-1; a variável i conta qual tentativa estamos.

# try: – começamos um bloco que pode gerar erro ao converter a entrada para inteiro.

# palpite = int(input(...)) – pede o palpite ao usuário e converte para int. A f-string mostra “Tentativa X/5”.

# except ValueError: – se o usuário digitar algo que não é número, cai aqui.

# mensagem de erro – avisa que a entrada é inválida.

# continue – pula para a próxima iteração do for. (Observação: isso faz com que a tentativa conte mesmo sendo inválida, pois o for avança o i.)

# linha em branco – separação visual.

# if palpite == numero_secreto: – verifica se acertou exatamente o número.

# mensagem de acerto – parabeniza o jogador.

# break – sai do for imediatamente (não gasta as tentativas restantes).

# elif palpite < numero_secreto: – se errou e o palpite foi menor, dá uma dica.

# mensagem – diz que o número secreto é maior que o palpite.

# else: – caso contrário, o palpite foi maior que o número secreto.

# mensagem – diz que o número secreto é menor que o palpite.

# else: (do for) – este else especial só executa se o for terminar sem break (ou seja, o jogador não acertou em nenhuma tentativa).

# mensagem – informa que as tentativas acabaram.

# mensagem – revela qual era o número secreto.

# linha em branco – separação visual.

# jogar_novamente = input(...).lower() – pergunta se quer jogar de novo e converte a resposta para minúsculas ('S' vira 's').

# if jogar_novamente != 's': – se a resposta não for 's', vamos sair do laço principal.

# break – interrompe o while True, encerrando o programa.

# linha em branco – separação visual.

# mensagem final – agradece por jogar, aparece quando saímos do while.