
# Nome do arquivo JSON
JSON_FILE = "financeiro.json"

def carregar_dados():
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(novo_dado):
    dados = carregar_dados()
    dados.append(novo_dado)
    with open(JSON_FILE, "w") as f:
        json.dump(dados, f, indent=4)

def adicionar():
    empresa = entry_empresa.get()
    rendimento = entry_rendimento.get()
    salario = entry_salario.get()
    impostos = entry_impostos.get()
    manutencao = entry_manutencao.get()
    
    if not empresa or not rendimento or not salario or not impostos or not manutencao:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        return
    
    novo_dado = {
        "Empresa": empresa,
        "Rendimento": float(rendimento),
        "Salário": float(salario),
        "Impostos": float(impostos),
        "Manutenção": float(manutencao)
    }
    salvar_dados(novo_dado)
    
    lista.insert(tk.END, f"{empresa} - R$ {rendimento}")
    entry_empresa.delete(0, tk.END)
    entry_rendimento.delete(0, tk.END)
    entry_salario.delete(0, tk.END)
    entry_impostos.delete(0, tk.END)
    entry_manutencao.delete(0, tk.END)
    atualizar_grafico()

def carregar_lista():
    dados = carregar_dados()
    for item in dados:
        lista.insert(tk.END, f"{item['Empresa']} - R$ {item['Rendimento']}")

def atualizar_grafico():
    dados = carregar_dados()
    if not dados:
        return
    
    empresas = [d["Empresa"] for d in dados]
    rendimentos = [d["Rendimento"] for d in dados]
    salarios = [d["Salário"] for d in dados]
    impostos = [d["Impostos"] for d in dados]
    manutencao = [d["Manutenção"] for d in dados]
    
    fig, ax = plt.subplots()
    ax.bar(empresas, rendimentos, label="Rendimento", color='green')
    ax.bar(empresas, salarios, label="Salário", color='blue', alpha=0.7)
    ax.bar(empresas, impostos, label="Impostos", color='red', alpha=0.7)
    ax.bar(empresas, manutencao, label="Manutenção", color='orange', alpha=0.7)
    
    ax.set_ylabel("Valores em R$")
    ax.set_title("Comparação Financeira das Empresas")
    ax.legend()
    
    for widget in frame_grafico.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Criando a interface gráfica
root = tk.Tk()
root.title("Sistema de Gerenciamento Financeiro")
root.attributes('-fullscreen', True)

frame_form = tk.Frame(root)
frame_form.pack(pady=20)

# Labels e Entrys
tk.Label(frame_form, text="Empresa:").grid(row=0, column=0)
entry_empresa = tk.Entry(frame_form)
entry_empresa.grid(row=0, column=1)

tk.Label(frame_form, text="Rendimento (R$):").grid(row=1, column=0)
entry_rendimento = tk.Entry(frame_form)
entry_rendimento.grid(row=1, column=1)

tk.Label(frame_form, text="Salário (R$):").grid(row=2, column=0)
entry_salario = tk.Entry(frame_form)
entry_salario.grid(row=2, column=1)

tk.Label(frame_form, text="Impostos (R$):").grid(row=3, column=0)
entry_impostos = tk.Entry(frame_form)
entry_impostos.grid(row=3, column=1)

tk.Label(frame_form, text="Manutenção (R$):").grid(row=4, column=0)
entry_manutencao = tk.Entry(frame_form)
entry_manutencao.grid(row=4, column=1)

# Botão para adicionar
tk.Button(frame_form, text="Adicionar", command=adicionar).grid(row=5, column=0, columnspan=2)

# Lista para exibir os dados
lista = tk.Listbox(root, width=50)
lista.pack(pady=10)

# Frame para o gráfico
frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=20)

# Botão para sair
tk.Button(root, text="Sair", command=root.quit).pack(pady=10)

# Carregar dados existentes
carregar_lista()
atualizar_grafico()

root.mainloop()
