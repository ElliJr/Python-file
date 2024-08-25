import tkinter as tk
import random

# Respostas pré-definidas do chatbot
responses = {
    "oi": ["Olá! Como posso ajudar você hoje?", "Oi! Como você está?", "Olá! O que posso fazer por você?"],
    "opa": ["Olá! Como posso ajudar você hoje?", "Oi! Como você está?", "Olá! O que posso fazer por você?"],
    "tudo bem": ["Estou bem, obrigado! E você?", "Tudo ótimo por aqui! E com você?", "Estou bem! Como posso ajudar?"],
    "qual seu nome": ["Me chamo Lav, uma bot inspirada na namorada do meu criador"],
    "qual é o seu nome": ["Eu sou um chatbot simples. Qual é o seu nome?", "Sou um chatbot criado em Python. Como posso ajudá-lo?"],
    "seu nome é ?": ["Eu sou um chatbot simples. Qual é o seu nome?", "Sou um chatbot criado em Python. Como posso ajudá-lo?"],
    "seu nome é ": ["Eu sou um chatbot simples. Qual é o seu nome?", "Sou um chatbot criado em Python. Como posso ajudá-lo?"],
    "seu nome é qual": ["Eu sou um chatbot simples. Qual é o seu nome?", "Sou um chatbot criado em Python. Como posso ajudá-lo?"],
    "adeus": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "tchau": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "não": ["então vai se fuder seu merda"],
    "nao": ["então vai se fuder seu merda"],
    "filha da puta": ["fala o que vc quiser seu bostinha eu não tenho mãe mesmo"],
    "vai se fuder": ["vai vc desgraça"],
}

# Função que encontra a resposta apropriada
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Não entendi o que vc disse com essa sua dicção, vc pode falar de novo?"

# Função para enviar mensagem
def send_message():
    user_input = entry.get()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "Você: " + user_input + "\n")
    entry.delete(0, tk.END)

    response = get_response(user_input)
    chat_history.insert(tk.END, "Lav: " + response + "\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Lav")

chat_history = tk.Text(root, bd=1, bg="lightgrey", width=50, height=20, wrap=tk.WORD, state=tk.DISABLED)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = tk.Entry(root, bd=1, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Enviar", width=10, command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
