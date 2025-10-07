import tkinter as tk

def clique():
    label.config(text="Você clicou no botão!")

# Criar janela
janela = tk.Tk()
janela.title("Minha primeira interface")

# Criar botão
botao = tk.Button(janela, text="Clique aqui", command=clique)
botao.pack(pady=10)

# Texto que será atualizado
label = tk.Label(janela, text="")
label.pack(pady=10)

# Rodar a janela
janela.mainloop()
