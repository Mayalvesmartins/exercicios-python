# util_saudacao.py

def boas_vindas(nome="usuário"):
    """
    Retorna uma mensagem de boas-vindas.

    Parâmetros:
        nome (str, opcional): Nome da pessoa. Padrão = "usuário".

    Retorna:
        str: Mensagem de boas-vindas.
    """
    return f"Olá, {nome}! Seja bem-vindo(a)!"


def despedida(nome="usuário"):
    """
    Retorna uma mensagem de despedida.

    Parâmetros:
        nome (str, opcional): Nome da pessoa. Padrão = "usuário".

    Retorna:
        str: Mensagem de despedida.
    """
    return f"Até logo, {nome}! Volte sempre!"


def elogio(nome="usuário"):
    """
    Retorna um elogio personalizado.

    Parâmetros:
        nome (str, opcional): Nome da pessoa. Padrão = "usuário".

    Retorna:
        str: Elogio.
    """
    return f"{nome}, você está fazendo um ótimo trabalho!"
