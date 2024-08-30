import tkinter as tk
import random
import wikipedia
import speech_recognition as sr
import pyttsx3
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
def abrir_link4():
    url = "https://ellijr.github.io/"
    webbrowser.open(url)

# Inicializa o motor de TTS (text-to-speech)
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade da fala
engine.setProperty('volume', 25)  # Nível de volume

# Respostas pré-definidas do chatbot
responses = {
    "tudo bem": ["Estou bem, obrigado! E você?", "Tudo ótimo por aqui! E com você?", "Estou bem! Como posso ajudar?", "Melhor agora 😃"],
    "melhor agora": ["que bom"],
    "qual seu nome": ["Me chamo Lav, uma bot inspirada na namorada do meu criador"],
    "quem te deu esse nome?": ["Esse nome láv, foi inspirado na linda namorada de meu criador, Lavínia "],
    "quem te deu esse nome": ["Esse nome láv, foi inspirado na linda namorada de meu criador, Lavínia "],
    "Quem te deu esse nome": ["Esse nome láv, foi inspirado na linda da namorada de meu criador, Lavínia "],
    "Quem é você?": ["Me chamo Láv, uma bot inspirada na namorada do meu criador"],
    "Quem é você": ["Me chamo Láv, uma bot inspirada na namorada do meu criador"],
    "quem é você": ["Me chamo Láv, uma bot inspirada na namorada do meu criador"],
    "quem e você?": ["Me chamo Láv, uma bot inspirada na namorada do meu criador"],
    "quem é vc?": ["Me chamo Láv, uma bot inspirada na namorada do meu criador"],
    "quem e vc": ["Me chamo Láv, uma bot inspirada na namorada do meu criador"],
    "Quem e você?": ["Me chamo Láv, uma bot inspirada na namorada do meu criador"],
    "Quem te deu esse nome?": ["Me chamo Lav, uma bot inspirada na namorada do meu criador"],
    "qual é o seu nome": ["Eu sou um chatbot simples. Qual é o seu nome?", "Sou um chatbot criado em Python. Como posso ajudá-lo?"],
    "seu nome é ?": ["Eu sou um chatbot simples. Qual é o seu nome?", "Sou um chatbot criado em Python. Como posso ajudá-lo?"],
    "oque vc pode fazer":["Bom eu posso fazer pesqusas na web e também posso ser sua assistente"],
    "o que vc pode fazer":["Bom eu posso fazer pesqusas na web e também posso ser sua assistente"],
    "o que você pode fazer":["Bom eu posso fazer pesqusas na web e também posso ser sua assistente"],
    "Oque vc pode fazer":["Bom eu posso fazer pesqusas na web e também posso ser sua assistente"],
    "Oque você pode fazer":["Bom eu posso fazer pesqusas na web e também posso ser sua assistente"],
    "O que você pode fazer":["Bom eu posso fazer pesqusas na web e também posso ser sua assistente"],
    "O que vc pode fazer":["Bom eu posso fazer pesqusas na web e também posso ser sua assistente"],
    "seu nome é ": ["Eu sou um chatbot simples. Qual é o seu nome?", "Sou um chatbot criado em Python. Como posso ajudá-lo?"],
    "seu nome é qual": ["Eu sou um chatbot simples. Qual é o seu nome?", "Sou um chatbot criado em Python. Como posso ajudá-lo?"],
    "adeus": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "tchau": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "ate mais": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "Até mais": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "Ate mais": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    "até mais": ["já vai tarde.", "não foi ainda porque", "tchau nada, não quero te ver mais."],
    #"filha da puta": ["fala o que você quiser seu bostinha eu não tenho mãe mesmo"],
    "vai se fuder": ["vai vc desgraça"],
    "pesquisar": ["o que você quer saber"],
    "pesquisa": ["o que você quer saber"],
    "Obrigado": ["por nada😃"],
    "obrigado": ["por nada😃"],
    "Muito obrigado": ["por nada😃"],
    "muito obrigado": ["por nada😃"],
    "Lav": ["Oie", "fala meu bom", "opa"],
    "lav": ["Oie", "fala meu bom", "opa"],
    "oi lav": ["Oie"],
    "oi": ["Oie", "fala meu bom", "opa"],
    "Oi": ["Oie", "fala meu bom", "opa"],
    "Oi lav": ["Oie", "fala meu bom",],
    "Oi Lav": ["Oie", "fala meu bom", "opa"],
    "oi Lav": ["Oie", "fala meu bom", "opa"],
    "opa lav": ["Oie", "fala meu bom", "opa"],
    "opa Lav": ["Oie", "fala meu bom", "opa"],
    "opa": ["Oie", "fala meu bom", "opa"],
    "Opa Lav": ["Oie", "fala meu bom", "opa"],
    "Opa lav": ["Oie", "fala meu bom", "opa"],
    "você é muito legal": ["Obrigada😃"],
    "Você é muito legal": ["Obrigada😃"],
    "Vc é muito legal": ["Obrigada😃"],
    "vc é muito legal": ["Obrigada😃"],
    "vc é legal": ["Obrigada😃"],
    "Vc é legal": ["Obrigada😃"],
    "quem é seu criador": ["É um mano de 17 anos que ta aprendendo python "],
    " e ele é bom": ["É... ele ta no caminho kkk"],
    " ele é bom": ["É... ele ta no caminho kkk"],
    "ele é bom programando?": ["É...... ele ta no caminho kkk"],
    "ele é bom programando": ["É... ele ta no caminho kkk"],
    "me mostre a minha data de namoro": ["28/04/24"],
    "me mostre a data de namoro": ["28/04/24"],
    "data de namoro": ["28/04/24"],
    "Me conte uma piada": ["eu conheci um cara chamado Mauro, e Mauro conhece e Nésia, Nésia chamou Mauro para comer na casa dela, e Mauro disse tó indonésia"],
    "me conte uma piada": ["eu conheci um cara chamado Mauro, e Mauro conhece e Nésia, Nésia chamou Mauro para comer na casa dela, e Mauro disse tó indonésia"],
    "me conte uma piada boa": ["eu conheci um cara chamado Mauro, e Mauro conhece e Nésia, Nésia chamou Mauro para comer na casa dela, e Mauro disse tó indonésia"],
    "Me conte uma piada boa": ["eu conheci um cara chamado Mauro, e Mauro conhece e Nésia, Nésia chamou Mauro para comer na casa dela, e Mauro disse tó indonésia"],
    "eu disse piada boa": ["essa foi a melhor que eu encontrei kkkkkk"],
    "eu disse piada boa": ["essa foi a melhor que eu encontrei kkkkkk"],
    "vc pode criar imagens?": ["infelizmente não posso "],
    "você pode criar imagens": ["infelizmente não posso "],
    "diga oi para o heitor": ["oi Heitor, tudo bem?"],
    "chame o heitor": ["Heitooooooooooooor, estou te chamandoooooo"],
    "tudo bem sim e vc": ["Melhor agora 😃"],
    "quanto que é 1 + 1": ["hello word"],
    "Posso te fazer uma pergunta": ["No caso vai ser duas, tó de zoas pode perguntar me bom"],
    "posso te fazer uma pergunta": ["No caso vai ser duas, tó de zoas pode perguntar me bom"],
    "posso fazer uma pergunta": ["No caso vai ser duas, tó de zoas pode perguntar me bom"],
    "posso te fazer uma pergunta": ["No caso vai ser duas, tó de zoas pode perguntar me bom"],
    "qual seu código fonte": ["você quer mesmo saber(digite y para sim, n para não)"],
    "qual seu código": ["você quer mesmo saber(digite Y para sim, N para não)"],
    "qual seu codigo": ["você quer mesmo saber(digite Y para sim, N para não)"],
    "y": ["aqui vai ele...... Hello word otário  kkkkkkkkkkk não vou passar meu código fonte kkkkkkkkk😃"],
    "n": ["que pena"],
    "vc pode fazer pesquisa na web?": ["posso fazer pequisas, mas não sou tão boa quanto um chaTGPT da vida "],
    "vc pode fazer pesquisa na web": ["posso fazer pequisas, mas não sou tão boa quanto um chaTGPT da vida"],
    "diga a frase": ["pode deixar... Eu te apresento o poder da sakánade, ela inverte o senso de direção do oponente tornando tudo como um quebra cabeça, engraçado né, você nunca deve ter jogado video game... parece que você não notou, pra frente e pra trás, esquerda e direita tudo está invertido, com todas essas mudanças de direção é hora de se perguntar se você poderá lutar enquanto inverte tudo dentro da sua cabeça, bem vindo Aizem ao mundo invertido.... musicá incrivel no fundo "],
    "a frase": ["pode deixar... Eu te apresento o poder da sakánade, ela inverte o senso de direção do oponente tornando tudo como um quebra cabeça, engraçado né, você nunca deve ter jogado video game... parece que você não notou, pra frente e pra trás, esquerda e direita tudo está invertido, com todas essas mudanças de direção é hora de se perguntar se você poderá lutar enquanto inverte tudo dentro da sua cabeça, bem vindo Aizem ao mundo invertido.... musicá incrivel no fundo"]
}

# Função que encontra a resposta apropriada
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    # Usa Wikipedia se não encontrar resposta na base de dados
    try:
        wikipedia.set_lang("pt")
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
        chat_history.insert(tk.END, "Lav: Desculpe, não entendi o que você disse, talvez seja porque você usou abreviação. Reformule a pergunta sem abreviação\n")
        chat_history.yview(tk.END)
        falar("Desculpe, não entendi o que você disse, talvez seja porque você usou abreviação. Reformule a pergunta sem abreviação")
    except sr.RequestError:
        chat_history.insert(tk.END, "Lav: Desculpe, não consegui acessar o serviço de reconhecimento de voz.\n")
        chat_history.yview(tk.END)
        falar("Desculpe, não consegui acessar o serviço de reconhecimento de voz.")

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Lav🦋")
menu_barra = tk.Menu(root)
root.config(menu=menu_barra)

arquivo_menu1 = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Abrir site", menu=arquivo_menu1)
arquivo_menu1.add_command(label="👉COFFE", command=abrir_link,)
arquivo_menu1.add_command(label="👉CBFengenharia", command=abrir_link2)
arquivo_menu1.add_command(label="👉Portífolio", command=abrir_link3)
arquivo_menu1.add_command(label="👉GitHub", command=abrir_link4)

chat_history = tk.Text(root, bd=1, bg="lightgrey", width=80, height=20, wrap=tk.WORD, state=tk.DISABLED)
chat_history.grid(row=0,column=0, columnspan=2, padx=10, pady=10)
chat_history = PhotoImage(file="")

entry = tk.Entry(root, bd=1, background="lightgrey",border="1px", width=60)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, border="1px",bg="grey",text="Enviar", width=20, command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
