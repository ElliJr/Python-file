import tkinter as tk
import random
import wikipedia
import speech_recognition as sr
import pyttsx3

# Inicializa o motor de TTS (text-to-speech)
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade da fala
engine.setProperty('volume', 0.9)  # Nível de volume

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
    "bem": ["que legal"],
    "otimo": ["que legal"],
    "ótimo": ["que legal"],
    "Otimo": ["que legal"],
    "Ótimo": ["que legal"],
    "mal": ["que legal"],
    "estou ruim": ["que legal"],
    "muito ruim": ["que legal"],
    "nada bem": ["que legal"],
    "filha da puta": ["fala o que você quiser seu bostinha eu não tenho mãe mesmo"],
    "vai se fuder": ["vai vc desgraça"],
    "pesquisa": ["o que vc quer saber"],
    "meu pai morreu": ["grande merda isso kkkkkkkkkkkkkkkkkkkk"],
}

# Função que encontra a resposta apropriada
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    # Usa Wikipedia se não encontrar resposta na base de dados
    try:
        resposta = wikipedia.summary(user_input, sentences=1, auto_suggest=False)
        return resposta
    except wikipedia.exceptions.DisambiguationError as e:
        return f"A consulta pode se referir a várias coisas: {', '.join(e.options)}"
    except wikipedia.exceptions.PageError:
        return "Desculpe, não encontrei nenhuma página correspondente."
    except Exception as e:
        return f"Um erro ocorreu: {e}"

# Função para o assistente falar
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

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
    falar(response)

# Função para ouvir e processar comando de voz
def ouvir_voz():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)

    try:
        comando = reconhecedor.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        entry.delete(0, tk.END)
        entry.insert(0, comando)
        send_message()
    except sr.UnknownValueError:
        chat_history.insert(tk.END, "Lav: Desculpe, não entendi o que você disse.\n")
        chat_history.yview(tk.END)
        falar("Desculpe, não entendi o que você disse.")
    except sr.RequestError:
        chat_history.insert(tk.END, "Lav: Desculpe, não consegui acessar o serviço de reconhecimento de voz.\n")
        chat_history.yview(tk.END)
        falar("Desculpe, não consegui acessar o serviço de reconhecimento de voz.")

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Lav")

chat_history = tk.Text(root, bd=1, bg="lightgrey", width=50, height=20, wrap=tk.WORD, state=tk.DISABLED)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = tk.Entry(root, bd=1, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Enviar", width=10, command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

voice_button = tk.Button(root, text="Ouvir", width=10, command=ouvir_voz)
voice_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
