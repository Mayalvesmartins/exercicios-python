import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Listas para armazenar os dados
notas = []
boletos = []

# Funções
def cadastrar_nota():
    numero = entry_numero.get()
    valor = entry_valor.get()
    if numero and valor:
        notas.append({"numero_nota": numero, "valor": float(valor)})
        messagebox.showinfo("Sucesso", f"Nota {numero} cadastrada!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos.")

def cadastrar_boleto():
    numero = entry_numero.get()
    valor = entry_valor.get()
    if numero and valor:
        boletos.append({"numero_nota": numero, "valor_pago": float(valor)})
        messagebox.showinfo("Sucesso", f"Boleto {numero} cadastrado!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos.")

def gerar_relatorio():
    if not notas or not boletos:
        messagebox.showwarning("Erro", "Cadastre notas e boletos antes de gerar o relatório.")
        return
    
    df_notas = pd.DataFrame(notas)
    df_boletos = pd.DataFrame(boletos)
    
    notas_sem_boleto = df_notas[~df_notas["numero_nota"].isin(df_boletos["numero_nota"])]
    boletos_sem_nota = df_boletos[~df_boletos["numero_nota"].isin(df_notas["numero_nota"])]
    conferidos = pd.merge(df_notas, df_boletos, on="numero_nota", how="inner")
    
    with pd.ExcelWriter("relatorio_conferencia.xlsx") as writer:
        notas_sem_boleto.to_excel(writer, sheet_name="Notas sem boleto", index=False)
        boletos_sem_nota.to_excel(writer, sheet_name="Boletos sem nota", index=False)
        conferidos.to_excel(writer, sheet_name="Conferidos", index=False)
    
    messagebox.showinfo("Relatório", "Relatório gerado com sucesso!")

# Criar a janela principal
root = tk.Tk()
root.title("Controle de Notas e Boletos")
root.geometry("300x200")

# Labels e Entradas
tk.Label(root, text="Número da Nota").pack()
entry_numero = tk.Entry(root)
entry_numero.pack()

tk.Label(root, text="Valor").pack()
entry_valor = tk.Entry(root)
entry_valor.pack()

# Botões
tk.Button(root, text="Cadastrar Nota", command=cadastrar_nota).pack(pady=5)
tk.Button(root, text="Cadastrar Boleto", command=cadastrar_boleto).pack(pady=5)
tk.Button(root, text="Gerar Relatório", command=gerar_relatorio).pack(pady=5)

root.mainloop()

