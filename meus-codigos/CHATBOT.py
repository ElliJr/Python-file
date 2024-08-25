
import openai
import tkinter as tk


openai.api_key = 'sk-g1p1jZK39-bmqQr0hiY8ixgGf4Zw28rzrUXEm65bS0T3BlbkFJ12BVa2lRRLbsp6slAtYVQQ8SsSjGreg0-KO4nOLmEA'  # Substitua pela sua chave da API

def chatbot_response(prompt):
    try:
        response = openai.completions.create(
            model="gpt-3.5-turbo",
           # engine="text-davinci-003",  # ou "gpt-3.5-turbo" dependendo do modelo
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Erro: {str(e)}"

def send_message():
    user_input = entry.get()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "Você: " + user_input + "\n")
    entry.delete(0, tk.END)

    response = chatbot_response(user_input)
    chat_history.insert(tk.END, "Bot: " + response + "\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Chatbot")

chat_history = tk.Text(root, bd=1, bg="lightgrey", width=50, height=20, wrap=tk.WORD, state=tk.DISABLED)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = tk.Entry(root, bd=1, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Enviar", width=10, command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
