import tkinter as tk
from tkinter import messagebox

# Lista para armazenar as tarefas
tarefas = []

# Função para listar tarefas
def listar_tarefas():
    lista_texto = ""
    if tarefas:
        for i, tarefa in enumerate(tarefas, 1):
            lista_texto += f"{i}. {tarefa}\n"
    else:
        lista_texto = "Nenhuma tarefa na lista."
    return lista_texto

# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa:
        tarefas.append(tarefa)
        entry_tarefa.delete(0, tk.END)
        atualizar_lista()
    else:
        messagebox.showwarning("Entrada Inválida", "A tarefa não pode estar vazia.")

# Função para remover tarefa
def remover_tarefa():
    try:
        indice = int(entry_indice.get()) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            entry_indice.delete(0, tk.END)
            atualizar_lista()
            messagebox.showinfo("Tarefa Removida", f"Tarefa '{tarefa_removida}' removida.")
        else:
            messagebox.showwarning("Índice Inválido", "Índice fora do intervalo.")
    except ValueError:
        messagebox.showwarning("Entrada Inválida", "Digite um número válido.")

# Função para atualizar a lista de tarefas na interface
def atualizar_lista():
    texto_lista.config(state=tk.NORMAL)
    texto_lista.delete(1.0, tk.END)
    texto_lista.insert(tk.END, listar_tarefas())
    texto_lista.config(state=tk.DISABLED)

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Gerenciador de Tarefas")

# Área de texto para exibir tarefas
texto_lista = tk.Text(root, bd=1, bg="lightgrey", width=50, height=15, wrap=tk.WORD, state=tk.DISABLED)
texto_lista.pack(padx=10, pady=10)

# Campo de entrada para adicionar tarefas
entry_tarefa = tk.Entry(root, width=40)
entry_tarefa.pack(padx=10, pady=5)

# Botão para adicionar tarefas
btn_adicionar = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack(pady=5)

# Campo de entrada para remover tarefas
entry_indice = tk.Entry(root, width=10)
entry_indice.pack(padx=10, pady=5, side=tk.LEFT)

# Botão para remover tarefas
btn_remover = tk.Button(root, text="Remover Tarefa", command=remover_tarefa)
btn_remover.pack(pady=5, side=tk.LEFT)

# Atualiza a lista inicialmente
atualizar_lista()

# Inicia o loop principal da interface gráfica
root.mainloop()
