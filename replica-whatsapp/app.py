import tkinter as tk
from tkinter import ttk

# Configurações principais da janela
root = tk.Tk()
root.title("WhatsApp")
root.geometry("800x500")
root.configure(bg="#1e1e1e")

# Lista de contatos com histórico de mensagens
contacts = [
    {"phone": "11960637124", "name": "MINHA PRIN...", "message": "Se arruma logooo", "time": "05/11/2024", "messages": ["Oi meu amor", "Como você está?"]},
    {"phone": "11 939138383", "name": "Mãe", "message": "Deixa que vou compr...", "time": "12:10", "messages": ["Não esquece de trazer o pão"]},
    {"phone": "339988-9475", "name": "Pai", "message": "0:07", "time": "11:22", "messages": ["Tudo bem por aí?"]},
    {"phone": "11999049268", "name": "Márcio Segurança", "message": "Blz", "time": "Ontem", "messages": ["Oi Márcio, tudo certo?"]},
    {"phone": "11998448302", "name": "Sogro", "message": "Kkkkkkk", "time": "Ontem", "messages": ["Bom dia!"]}
]

# Dicionário de respostas automáticas
auto_responses = {
    "oi": "Oi meu amor",
    "tudo bem": "Estou bem, e você?",
    "qual seu nome?": "Meu nome é WhatsBot.",
    "olá": "Olá, como posso ajudar?",
    "como você está?": "Estou bem, obrigado por perguntar!"
}

current_contact = None

# Função para abrir a interface de chat do contato selecionado
def open_chat_by_phone(phone):
    global current_contact
    for contact in contacts:
        if contact["phone"] == phone:
            current_contact = contact
            main_screen()
            show_chat_window()
            return
    # Caso o número não seja encontrado
    error_label.config(text="Número não encontrado.")

# Função para mostrar a janela de conversa
def show_chat_window():
    for widget in chat_frame.winfo_children():
        widget.destroy()

    if current_contact:
        # Cabeçalho da conversa
        header_frame = tk.Frame(chat_frame, bg="#2a2f32")
        header_frame.pack(fill=tk.X)

        name_label = tk.Label(header_frame, text=current_contact["name"], font=("Arial", 14, "bold"), bg="#2a2f32", fg="white")
        name_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Área de mensagens
        messages_frame = tk.Frame(chat_frame, bg="#ece5dd")
        messages_frame.pack(fill=tk.BOTH, expand=True)

        # Mostrar mensagens
        for i, msg in enumerate(current_contact["messages"]):
            if i % 2 == 0:  # Respostas automáticas (lado esquerdo)
                message_label = tk.Label(messages_frame, text=msg, font=("Arial", 12), bg="#dcf8c6", fg="black", pady=5, padx=10)
                message_label.pack(anchor='e', pady=2, padx=10)
            else:  # Mensagens do usuário (lado direito)
                message_label = tk.Label(messages_frame, text=msg, font=("Arial", 12), bg="#128c7e", fg="white", pady=5, padx=10)
                message_label.pack(anchor='w', pady=2, padx=10)

        # Campo de entrada para enviar mensagens
        entry_frame = tk.Frame(chat_frame, bg="#2a2f32")
        entry_frame.pack(fill=tk.X)

        message_entry = tk.Entry(entry_frame, font=("Arial", 12), bg="#323739", fg="white")
        message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=10)

        # Função para enviar a mensagem
        def send_message(event=None):
            message = message_entry.get().lower()  # Convertendo para minúsculas para facilitar a comparação
            if message:
                current_contact["messages"].append(message)
                message_entry.delete(0, tk.END)
                show_chat_window()  # Atualiza a janela para exibir a nova mensagem

                # Simula a resposta automática com base na mensagem
                root.after(1000, simulate_response, message)

        # Botão de envio
        send_button = tk.Button(entry_frame, text="Enviar", command=send_message, bg="#128c7e", fg="white")
        send_button.pack(side=tk.RIGHT, padx=10)

        # Pressionar Enter também envia a mensagem
        message_entry.bind("<Return>", send_message)

# Função para simular uma resposta automática com base na mensagem
def simulate_response(user_message):
    if current_contact:
        response = auto_responses.get(user_message, "Desculpe, não entendi.")  # Resposta padrão se não encontrar a chave
        current_contact["messages"].append(response)
        show_chat_window()  # Atualiza a janela com a resposta

# Função para mostrar a tela principal
def main_screen():
    phone_frame.pack_forget()  # Oculta a tela inicial

    # Cabeçalho principal
    header_frame = tk.Frame(root, bg="#2a2f32")
    header_frame.pack(fill=tk.X)

    title_label = tk.Label(header_frame, text="Conversas", font=("Arial", 16), bg="#2a2f32", fg="white")
    title_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Ícones do cabeçalho
    icons_frame = tk.Frame(header_frame, bg="#2a2f32")
    icons_frame.pack(side=tk.RIGHT, padx=10)

    icon_1 = tk.Label(icons_frame, text="🔍", bg="#2a2f32", fg="white", font=("Arial", 16))
    icon_1.pack(side=tk.LEFT, padx=5)

    icon_2 = tk.Label(icons_frame, text="⚙️", bg="#2a2f32", fg="white", font=("Arial", 16))
    icon_2.pack(side=tk.LEFT, padx=5)

    # Área de pesquisa
    search_frame = tk.Frame(root, bg="#1e1e1e")
    search_frame.pack(fill=tk.X, padx=10, pady=10)

    search_entry = tk.Entry(search_frame, font=("Arial", 14), bg="#323739", fg="white", bd=0)
    search_entry.insert(0, "Pesquisar ou começar uma nova conversa")
    search_entry.pack(fill=tk.X, ipady=8)

    # Área de lista de contatos
    contacts_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5, side=tk.LEFT)
    chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5, side=tk.RIGHT)

# Tela inicial para inserir o número de telefone
phone_frame = tk.Frame(root, bg="#1e1e1e")
phone_frame.pack(fill=tk.BOTH, expand=True)

label = tk.Label(phone_frame, text="Digite o número de telefone:", font=("Arial", 14), bg="#1e1e1e", fg="white")
label.pack(pady=20)

phone_entry = tk.Entry(phone_frame, font=("Arial", 14), bg="#323739", fg="white")
phone_entry.pack(ipady=8)

error_label = tk.Label(phone_frame, text="", font=("Arial", 10), bg="#1e1e1e", fg="red")
error_label.pack()

enter_button = tk.Button(phone_frame, text="Entrar", command=lambda: open_chat_by_phone(phone_entry.get()), bg="#128c7e", fg="white")
enter_button.pack(pady=10)

# Área de lista de contatos e de chat
contacts_frame = tk.Frame(root, bg="#131c21")
chat_frame = tk.Frame(root, bg="#ece5dd")

# Iniciar a aplicação
root.mainloop()
