import tkinter as tk
from tkinter import messagebox
import json

# Nome do arquivo JSON
JSON_FILE = "dados.json"

def carregar_dados():
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(novo_dado):
    dados = carregar_dados()
    dados.append(novo_dado)
    with open(JSON_FILE, "w") as f:
        json.dump(dados, f, indent=4)

def adicionar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()
    
    if not nome or not cpf or not telefone:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        return
    
    novo_dado = {"Nome": nome, "CPF": cpf, "Telefone": telefone}
    salvar_dados(novo_dado)
    
    lista.insert(tk.END, f"{nome} - {cpf} - {telefone}")
    entry_nome.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

def carregar_lista():
    dados = carregar_dados()
    for item in dados:
        lista.insert(tk.END, f"{item['Nome']} - {item['CPF']} - {item['Telefone']}")

# Criando a interface gráfica
root = tk.Tk()
root.title("Cadastro de Pessoas")

# Labels e Entrys
tk.Label(root, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="CPF:").grid(row=1, column=0)
entry_cpf = tk.Entry(root)
entry_cpf.grid(row=1, column=1)

tk.Label(root, text="Telefone:").grid(row=2, column=0)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1)

# Botão para adicionar
tk.Button(root, text="Adicionar", command=adicionar).grid(row=3, column=0, columnspan=2)

# Lista para exibir os dados
lista = tk.Listbox(root, width=50)
lista.grid(row=4, column=0, columnspan=2)

# Carregar dados existentes
carregar_lista()

root.mainloop()
