import tkinter as tk

def iniciar_peneira():
    print("iniciando peneira")

janela = tk.Tk()
janela.title("peneira tecnológica")
janela.geometry("280x50")

botao_iniciar = tk.Button(janela, bg="grey",text="iniciar", command=iniciar_peneira)
botao_iniciar.pack()

janela.mainloop() 