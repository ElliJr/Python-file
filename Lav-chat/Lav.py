import tkinter as tk
from tkinter import ttk
import random
import webbrowser

def abrir_link():
    url = "https://ellijr.github.io/COFFE--Site/"
    webbrowser.open(url)

def abrir_link2():
    url = "https://ellijr.github.io/CBFengenharia/"
    webbrowser.open(url)

def abrir_link3():
    url = "https://ellijr.github.io/portifolio/"
    webbrowser.open(url)
responses = {
    "tudo bem": ["estou bem, obrigado! e você?", "tudo ótimo por aqui! e com você?", "estou bem! como posso ajudar?", "melhor agora 😃"],
    "melhor agora": ["que bom"],
    "qual seu nome": ["me chamo lav, uma bot inspirada na namorada do meu criador"],
    "quem te deu esse nome?": ["esse nome láv, foi inspirado na linda namorada de meu criador, lavínia"],
    "quem te deu esse nome": ["esse nome láv, foi inspirado na linda namorada de meu criador, lavínia"],
    "quem é você?": ["me chamo láv, uma bot inspirada na namorada do meu criador"],
    "quem é você": ["me chamo láv, uma bot inspirada na namorada do meu criador"],
    "quem e você?": ["me chamo láv, uma bot inspirada na namorada do meu criador"],
    "quem é vc?": ["me chamo láv, uma bot inspirada na namorada do meu criador"],
    "quem e vc": ["me chamo láv, uma bot inspirada na namorada do meu criador"],
    "qual é o seu nome": ["eu sou um chatbot simples. qual é o seu nome?", "sou um chatbot criado em python. como posso ajudá-lo?"],
    "seu nome é ?": ["eu sou um chatbot simples. qual é o seu nome?", "sou um chatbot criado em python. como posso ajudá-lo?"],
    "oque vc pode fazer": ["bom eu posso fazer pesquisas na web e também posso ser sua assistente"],
    "o que vc pode fazer": ["bom eu posso fazer pesquisas na web e também posso ser sua assistente"],
    "o que você pode fazer": ["bom eu posso fazer pesquisas na web e também posso ser sua assistente"],
    "adeus": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "tchau": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "até mais": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "vai se fuder": ["vai vc desgraça"],
    "pesquisar": ["o que você quer saber"],
    "pesquisa": ["o que você quer saber"],
    "obrigado": ["por nada😃"],
    "muito obrigado": ["por nada😃"],
    "lav": ["oie", "fala meu bom", "opa"],
    "oi lav": ["oie"],
    "oi": ["oie", "fala meu bom", "opa"],
    "opa lav": ["oie", "fala meu bom", "opa"],
    "opa": ["oie", "fala meu bom", "opa"],
    "você é muito legal": ["obrigada😃"],
    "vc é muito legal": ["obrigada😃"],
    "quem é seu criador": ["é um mano de 17 anos que tá aprendendo python"],
    "e ele é bom": ["é... ele tá no caminho kkk"],
    "ele é bom programando?": ["é... ele tá no caminho kkk"],
    "me mostre a minha data de namoro": ["28/04/24"],
    "data de namoro": ["28/04/24"],
    "namoro": ["28/04/24"],
    "me conte uma piada": ["eu conheci um cara chamado mauro, e mauro conhece e nésia, nésia chamou mauro para comer na casa dela, e mauro disse tó indonésia"],
    "me conte uma piada boa": ["eu conheci um cara chamado mauro, e mauro conhece e nésia, nésia chamou mauro para comer na casa dela, e mauro disse tó indonésia"],
    "eu disse piada boa": ["essa foi a melhor que eu encontrei kkkkkk"],
    "vc pode criar imagens?": ["infelizmente não posso"],
    "diga oi para o heitor": ["oi heitor, tudo bem?"],
    "chame o heitor": ["heitooooooooooooor, estou te chamandoooooo"],
    "tudo bem sim e vc": ["melhor agora 😃"],
    "quanto que é 1 + 1": ["hello world"],
    "posso te fazer uma pergunta": ["no caso vai ser duas, tó de zoas pode perguntar me bom"],
    "qual seu código fonte": ["você quer mesmo saber (digite y para sim, n para não)"],
    "qual seu código": ["você quer mesmo saber (digite y para sim, n para não)"],
    "y": ["aqui vai ele... hello world otário kkkkkkkkkk não vou passar meu código fonte kkkkkkkkk😃"],
    "vc pode fazer pesquisa na web?": ["posso fazer pesquisas, mas não sou tão boa quanto um chatgpt da vida"],
    "diga a frase": ["pode deixar... eu te apresento o poder da sakánade, ela inverte o senso de direção do oponente tornando tudo como um quebra-cabeça, engraçado né, você nunca deve ter jogado video game... parece que você não notou, pra frente e pra trás, esquerda e direita tudo está invertido, com todas essas mudanças de direção é hora de se perguntar se você poderá lutar enquanto inverte tudo dentro da sua cabeça, bem vindo aizem ao mundo invertido... música incrível no fundo"],
    "fala para o heitor ir tomar banho": ["vai tomar banho cagão"],
    "ele disse que não quer ir tomar banho": ["oque?, eu vou chamar a mãe dele"],
    "": ["se certifique de ter escrito algo mano"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Desculpe, não entendi isso."

def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"Você: {user_input}\n")
    entry.delete(0, tk.END)

    response = get_response(user_input)
    chat_history.insert(tk.END, f"Lav: {response}\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)

root = tk.Tk()
root.title("Lav🦋")
root.geometry("500x400")
root.configure(bg="black")

menu_barra = tk.Menu(root)
root.config(menu=menu_barra)

arquivo_menu1 = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Abrir site", menu=arquivo_menu1)
arquivo_menu1.add_command(label="👉 COFFE", command=abrir_link)
arquivo_menu1.add_command(label="👉 CBFengenharia", command=abrir_link2)
arquivo_menu1.add_command(label="👉 Portfólio", command=abrir_link3)

chat_history = tk.Text(root, bg="#2d2d2d", fg="white", width=58, height=15, wrap=tk.WORD, state=tk.DISABLED)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = ttk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = ttk.Button(root, text="Enviar", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
