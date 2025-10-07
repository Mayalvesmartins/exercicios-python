import tkinter as tk

def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa != "":
        lista.insert(tk.END, tarefa)  # adiciona no final da lista
        entrada.delete(0, tk.END)     # limpa a caixa de texto

def remover_tarefa():
    selecionada = lista.curselection()  # pega o item marcado
    if selecionada:
        lista.delete(selecionada)

# Criar a janela
janela = tk.Tk()
janela.title("Lista de Tarefas")

# Caixa de texto para digitar tarefa
entrada = tk.Entry(janela, width=40)
entrada.pack(pady=5)

# Botão para adicionar
botao_add = tk.Button(janela, text="Adicionar", command=adicionar_tarefa)
botao_add.pack(pady=5)

# Lista de tarefas
lista = tk.Listbox(janela, width=50, height=10)
lista.pack(pady=5)

# Botão para remover
botao_del = tk.Button(janela, text="Remover", command=remover_tarefa)
botao_del.pack(pady=5)

# Iniciar o app
janela.mainloop()
