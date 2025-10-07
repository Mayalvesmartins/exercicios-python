import tkinter as tk

def adicionar_numero(numero):
    entrada_var.set(entrada_var.get() + str(numero))

def adicionar_operacao(operacao):
    entrada_var.set(entrada_var.get() + operacao)

def calcular():
    try:
        resultado = eval(entrada_var.get())
        entrada_var.set(str(resultado))
    except:
        entrada_var.set("Erro")

def limpar():
    entrada_var.set("")

# Criar janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

# Variável da tela
entrada_var = tk.StringVar()

# Tela da calculadora
entrada = tk.Entry(janela, textvariable=entrada_var, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entrada.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Frame para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack()

# Lista de botões
botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Criar botões dinamicamente
for i, linha in enumerate(botoes):
    for j, botao in enumerate(linha):
        if botao == "=":
            b = tk.Button(frame_botoes, text=botao, width=5, height=2, font=("Arial", 15), command=calcular)
        elif botao == "C":
            b = tk.Button(frame_botoes, text=botao, width=5, height=2, font=("Arial", 15), command=limpar)
        elif botao in "+-*/":
            b = tk.Button(frame_botoes, text=botao, width=5, height=2, font=("Arial", 15), command=lambda op=botao: adicionar_operacao(op))
        else:
            b = tk.Button(frame_botoes, text=botao, width=5, height=2, font=("Arial", 15), command=lambda num=botao: adicionar_numero(num))
        b.grid(row=i, column=j, padx=5, pady=5)

# Rodar a janela
janela.mainloop()
