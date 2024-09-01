import tkinter as tk
import webbrowser
from tkinter import filedialog, messagebox

def abrir_link():    
    url = "https://ellijr.github.io/COFFE--Site/"
    webbrowser.open(url)
def abrir_link2():
    url = "https://ellijr.github.io/CBFengenharia/"
    webbrowser.open(url)
def abrir_link3():
    url = "https://ellijr.github.io/portifolio/"
    webbrowser.open(url)

def novo_arquivo():
    texto.delete(1.0, tk.END)

def abrir_arquivo():
    caminho_arquivo = filedialog.askopenfilename(defaultextension=".txt", 
                                                 filetypes=[("Arquivos de texto", "*.txt"), 
                                                            ("Todos os arquivos", "*.*")])
    if caminho_arquivo:
        with open(caminho_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, conteudo)

def salvar_arquivo():
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                   filetypes=[("Arquivos de texto", "*.txt"), 
                                                              ("Todos os arquivos", "*.*")])
    if caminho_arquivo:
        with open(caminho_arquivo, "w") as arquivo:
            conteudo = texto.get(1.0, tk.END)
            arquivo.write(conteudo)
            messagebox.showinfo("Salvido", "Teu arquivo foi salvo manin!😃")

# Configurar a janela principal
janela = tk.Tk()
janela.title("APP do Elli")

# Adicionar uma área de texto
texto = tk.Text(janela, wrap='word')
texto.pack(expand=True, fill='both')

# Adicionar um menu
menu_barra = tk.Menu(janela)
janela.config(menu=menu_barra)


arquivo_menu = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Menu", menu=arquivo_menu)
arquivo_menu.add_command(label="👉Novo", command=novo_arquivo)
arquivo_menu.add_command(label="👉Abrir", command=abrir_arquivo)
arquivo_menu.add_command(label="👉Salvar Como", command=salvar_arquivo)
arquivo_menu.add_command(label="👉Sair", command=janela.quit)

arquivo_menu1 = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Abrir site", menu=arquivo_menu1)
arquivo_menu1.add_command(label="👉COFFE", command=abrir_link,)
arquivo_menu1.add_command(label="👉CBFengenharia", command=abrir_link2)
arquivo_menu1.add_command(label="👉Portífolio", command=abrir_link3)
# Executar o aplicativo
janela.mainloop()
