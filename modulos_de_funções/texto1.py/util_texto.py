def capitalizar(texto):
    """
    Capitaliza a primeira letra de cada palavra do texto.

    Parâmetros:
        texto (str): O texto a ser capitalizado.

    Retorna:
        str: Texto com a primeira letra de cada palavra em maiúscula.
    """
    return texto.title()


def contar_palavras(texto):
    """
    Conta o número de palavras no texto.

    Parâmetros:
        texto (str): O texto para contar as palavras.

    Retorna:
        int: A quantidade de palavras.
    """
    return len(texto.split())


def inverter_texto(texto):
    """
    Inverte todos os caracteres do texto.

    Parâmetros:
        texto (str): O texto a ser invertido.

    Retorna:
        str: O texto invertido.
    """
    return texto[::-1]
