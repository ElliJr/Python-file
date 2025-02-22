import tkinter as tk

# Função para atualizar a entrada
def clicar(botao):
    entrada.insert(tk.END, botao)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 20), justify="right")
entrada.pack(fill="both", padx=10, pady=10)

# Botões da calculadora
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

# Criando os botões
frame = tk.Frame(janela)
frame.pack()

linha = 0
coluna = 0

for botao in botoes:
    comando = lambda x=botao: clicar(x) if x not in ["C", "="] else (limpar() if x == "C" else calcular())

    tk.Button(frame, text=botao, width=5, height=2, font=("Arial", 14),
              command=comando).grid(row=linha, column=coluna)

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Rodar a interface
janela.mainloop()
