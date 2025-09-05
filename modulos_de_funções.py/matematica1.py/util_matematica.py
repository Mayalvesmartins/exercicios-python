# util_matematica.py

def dobro(numero):
    """
    Retorna o dobro de um número.

    Parâmetros:
        numero (int/float): O número a ser dobrado.

    Retorna:
        int/float: O dobro do número.
    """
    return numero * 2


def raiz_quadrada(numero):
    """
    Retorna a raiz quadrada de um número.

    Parâmetros:
        numero (int/float): O número para calcular a raiz.

    Retorna:
        float: A raiz quadrada do número.
    """
    return numero ** 0.5


def celsius_para_fahrenheit(celsius=0):
    """
    Converte temperatura de Celsius para Fahrenheit.

    Parâmetros:
        celsius (float, opcional): Temperatura em Celsius (padrão = 0).

    Retorna:
        float: Temperatura em Fahrenheit.
    """
    return (celsius * 9/5) + 32
