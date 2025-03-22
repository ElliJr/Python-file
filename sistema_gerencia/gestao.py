import tkinter as tk
from tkinter import ttk, messagebox
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Aplicativo:
    def __init__(self, root):
        self.root = root
        self.root.title(" EL Enterprise Language⚙️")
        self.root.geometry("1300x800")
        
        # Cores
        self.cor_principal = "#1E3A5F"  # Azul escuro
        self.cor_secundaria = "#2C5EAA"  # Azul médio
        self.cor_destaque = "#D9A87E"  # Marrom suave
        self.cor_fonte = "white"
        
        # Tela de login
        self.login_tela()

    def login_tela(self):
        self.login_frame = tk.Frame(self.root, bg=self.cor_principal)
        self.login_frame.pack(fill=tk.BOTH, expand=True)
        
        label_titulo = tk.Label(self.login_frame, text="Sistema de Gerenciamento", font=("Arial", 24), fg=self.cor_fonte, bg=self.cor_principal)
        label_titulo.pack(pady=20)
        
        label_usuario = tk.Label(self.login_frame, text="Usuário:", font=("Arial", 14), fg=self.cor_fonte, bg=self.cor_principal)
        label_usuario.pack(pady=5)
        self.entry_usuario = tk.Entry(self.login_frame, font=("Arial", 14))
        self.entry_usuario.pack(pady=5)
        
        label_senha = tk.Label(self.login_frame, text="Senha:", font=("Arial", 14), fg=self.cor_fonte, bg=self.cor_principal)
        label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(self.login_frame, font=("Arial", 14), show="*")
        self.entry_senha.pack(pady=5)
        
        botao_entrar = tk.Button(self.login_frame, text="Entrar", font=("Arial", 14), bg=self.cor_secundaria, fg=self.cor_fonte, command=self.verificar_login)
        botao_entrar.pack(pady=20)
        
        botao_cadastro = tk.Button(self.login_frame, text="Cadastrar", font=("Arial", 14), bg=self.cor_secundaria, fg=self.cor_fonte, command=self.cadastro_tela)
        botao_cadastro.pack(pady=10)

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        # Carregar usuários registrados
        usuarios = self.carregar_usuarios()
        
        if usuario in usuarios and usuarios[usuario] == senha:
            self.login_frame.pack_forget()
            self.iniciar_sistema()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
    
    def cadastro_tela(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Cadastro de Conta")
        nova_janela.geometry("400x300")
        
        label_usuario = tk.Label(nova_janela, text="Usuário:", font=("Arial", 14))
        label_usuario.pack(pady=5)
        entry_usuario = tk.Entry(nova_janela, font=("Arial", 14))
        entry_usuario.pack(pady=5)
        
        label_senha = tk.Label(nova_janela, text="Senha:", font=("Arial", 14))
        label_senha.pack(pady=5)
        entry_senha = tk.Entry(nova_janela, font=("Arial", 14), show="*")
        entry_senha.pack(pady=5)
        
        def salvar_usuario():
            usuario = entry_usuario.get()
            senha = entry_senha.get()
            
            if not usuario or not senha:
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return
            
            # Salvar o usuário e senha no arquivo
            usuarios = self.carregar_usuarios()
            if usuario in usuarios:
                messagebox.showerror("Erro", "Usuário já existe.")
                return
            
            usuarios[usuario] = senha
            self.salvar_usuarios(usuarios)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            nova_janela.destroy()
        
        botao_salvar = tk.Button(nova_janela, text="Cadastrar", font=("Arial", 14), command=salvar_usuario)
        botao_salvar.pack(pady=20)
    
    def carregar_usuarios(self):
        try:
            with open("usuarios.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def salvar_usuarios(self, usuarios):
        with open("usuarios.json", "w") as file:
            json.dump(usuarios, file, indent=4)
    
    def iniciar_sistema(self):
        self.main_frame = tk.Frame(self.root, bg=self.cor_principal)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.sidebar = tk.Frame(self.main_frame, bg=self.cor_secundaria, width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        self.content_frame = tk.Frame(self.main_frame, bg="white")
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.paginas = {}
        
        botoes = ["Financeiro", "Vendas", "Compras", "Clientes", "Produtos", "Relatórios", "Configurações", "Suporte", "Conta"]
        for btn in botoes:
            self.criar_botao_personalizado(self.sidebar, btn)
        
        self.criar_paginas()
        self.mudar_pagina("Produtos")
        
    def criar_botao_personalizado(self, parent, texto):
        botao = tk.Button(parent, text=texto, font=("Arial", 12), bg=self.cor_secundaria, fg=self.cor_fonte, relief="raised", command=lambda: self.mudar_pagina(texto))
        botao.pack(fill=tk.X, padx=10, pady=5)
    
    def mudar_pagina(self, nome_pagina):
        for pagina in self.paginas.values():
            pagina.pack_forget()
        self.paginas[nome_pagina].pack(fill=tk.BOTH, expand=True)

    
    def criar_paginas(self):
        for nome in ["Financeiro", "Vendas", "Compras", "Clientes", "Produtos", "Relatórios", "Configurações", "Suporte", "Conta"]:
            frame = tk.Frame(self.content_frame, bg="white")
            label = tk.Label(frame, text=nome, font=("Arial", 24), bg="white")
            label.pack(pady=20)
            self.paginas[nome] = frame
        
        self.criar_pagina_produtos()
        self.criar_pagina_clientes()
        self.criar_pagina_conta()
        self.criar_pagina_Financeiro()
    
    def criar_pagina_produtos(self):
        frame = self.paginas["Produtos"]
        
        self.tree_produtos = ttk.Treeview(frame, columns=("#1", "#2", "#3", "#4", "#5"), show="headings")
        self.tree_produtos.heading("#1", text="Cód")
        self.tree_produtos.heading("#2", text="Produto")
        self.tree_produtos.heading("#3", text="Categoria")
        self.tree_produtos.heading("#4", text="Preço Venda")
        self.tree_produtos.heading("#5", text="Estoque")
        
        self.tree_produtos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.produtos = []
        self.carregar_dados("produtos.json", self.produtos, self.tree_produtos)
        
        self.secao_botoes_produtos = tk.Frame(frame, bg="white")
        self.secao_botoes_produtos.pack(pady=10)
        
        tk.Button(self.secao_botoes_produtos, text="+ Novo", font=("Arial", 12), bg=self.cor_secundaria, fg=self.cor_fonte, command=lambda: self.abrir_janela_novo("produtos.json", self.produtos, self.tree_produtos, ["Nome do Produto", "Categoria", "Preço", "Estoque"])).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.secao_botoes_produtos, text="Remover", font=("Arial", 12), bg=self.cor_secundaria, fg=self.cor_fonte, command=lambda: self.remover_item("produtos.json", self.produtos, self.tree_produtos)).grid(row=0, column=1, padx=10, pady=10)
    
    def criar_pagina_clientes(self):
        frame = self.paginas["Clientes"]
        
        self.tree_clientes = ttk.Treeview(frame, columns=("#1", "#2", "#3", "#4"), show="headings")
        self.tree_clientes.heading("#1", text="Nome")
        self.tree_clientes.heading("#2", text="CPF")
        self.tree_clientes.heading("#3", text="Email")
        self.tree_clientes.heading("#4", text="Telefone")
        
        self.tree_clientes.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.clientes = []
        self.carregar_dados("clientes.json", self.clientes, self.tree_clientes)
        
        self.secao_botoes_clientes = tk.Frame(frame, bg="white")
        self.secao_botoes_clientes.pack(pady=10)
        
        tk.Button(self.secao_botoes_clientes, text="+ Novo", font=("Arial", 12), bg=self.cor_secundaria, fg=self.cor_fonte, command=lambda: self.abrir_janela_novo("clientes.json", self.clientes, self.tree_clientes, ["Nome", "CPF", "Email", "Telefone"])).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.secao_botoes_clientes, text="Remover", font=("Arial", 12), bg=self.cor_secundaria, fg=self.cor_fonte, command=lambda: self.remover_item("clientes.json", self.clientes, self.tree_clientes)).grid(row=0, column=1, padx=10, pady=10)
    
    def criar_pagina_Financeiro(self):
        frame = self.paginas["Financeiro"]




    def criar_pagina_conta(self):
        frame = self.paginas["Conta"]
        
        label_conta = tk.Label(frame, text="Monitoramento da Conta", font=("Arial", 24), bg="white")
        label_conta.pack(pady=20)
        
        self.conta_info = self.carregar_dados_conta("usuarios.json")
        
        label_nome = tk.Label(frame, text=f"Nome: {self.conta_info['nome']}", font=("Arial", 14), bg="white")
        label_nome.pack(pady=10)
        
        label_email = tk.Label(frame, text=f"Email: {self.conta_info['email']}", font=("Arial", 14), bg="white")
        label_email.pack(pady=10)
        
        label_telefone = tk.Label(frame, text=f"Telefone: {self.conta_info['telefone']}", font=("Arial", 14), bg="white")
        label_telefone.pack(pady=10)
        
        tk.Button(frame, text="Editar Conta", font=("Arial", 12), bg=self.cor_secundaria, fg=self.cor_fonte, command=self.abrir_janela_editar_conta).pack(pady=20)
    
    def carregar_dados_usuarios(self, arquivo):
        try:
            with open(arquivo, "r") as file:
                usuarios = json.load(file)
            # Verificar se as informações completas existem
            if isinstance(usuarios, dict):
                if "nome" not in usuarios or "email" not in usuarios or "telefone" not in usuarios:
                    return False  # Significa que falta dados
            return usuarios
        except FileNotFoundError:
            return False  # Arquivo não encontrado

    
    
    def carregar_dados(self, arquivo, lista, tree):
        try:
            with open(arquivo, "r") as file:
                lista.extend(json.load(file))
                for item in lista:
                    tree.insert("", "end", values=item)
        except FileNotFoundError:
            pass
    
    def salvar_dados(self, arquivo, lista):
        with open(arquivo, "w") as file:
            json.dump(lista, file, indent=4)
    


    def abrir_janela_editar_conta(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Editar Conta")
        nova_janela.geometry("400x300")
        
        entradas = []
        campos = ["Nome", "Email", "Telefone"]
        
        for campo in campos:
            tk.Label(nova_janela, text=campo + ":").pack(pady=5)
            entry = tk.Entry(nova_janela)
            entry.insert(0, self.conta_info[campo.lower()])
            entry.pack(pady=5)
            entradas.append(entry)
        
        def salvar_edicoes():
            for idx, campo in enumerate(campos):
                self.conta_info[campo.lower()] = entradas[idx].get()
            with open("conta.json", "w") as file:
                json.dump(self.conta_info, file, indent=4)
            nova_janela.destroy()
            self.criar_pagina_conta()  # Atualiza a página de conta
        
        tk.Button(nova_janela, text="Salvar", command=salvar_edicoes).pack(pady=10)
    
    def carregar_dados(self, arquivo, lista, tree):
        try:
            with open(arquivo, "r") as file:
                lista.extend(json.load(file))
                for item in lista:
                    tree.insert("", "end", values=item)
        except FileNotFoundError:
            pass
    
    def salvar_dados(self, arquivo, lista):
        with open(arquivo, "w") as file:
            json.dump(lista, file, indent=4)
    
    def remover_item(self, arquivo, lista, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um item para remover.")
            return
        for item in selecionado:
            valores = tree.item(item, "values")
            lista.remove(list(valores))
            tree.delete(item)
        self.salvar_dados(arquivo, lista)
    
    def abrir_janela_novo(self, arquivo, lista, tree, campos):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Adicionar Novo Registro")
        nova_janela.geometry("400x300")
        
        entradas = []
        for campo in campos:
            tk.Label(nova_janela, text=campo + ":").pack(pady=5)
            entry = tk.Entry(nova_janela)
            entry.pack(pady=5)
            entradas.append(entry)
        
        def adicionar():
            novo_item = [entry.get() for entry in entradas]
            lista.append(novo_item)
            tree.insert("", "end", values=novo_item)
            self.salvar_dados(arquivo, lista)
            nova_janela.destroy()
        
        tk.Button(nova_janela, text="Adicionar", command=adicionar).pack(pady=10)


    def remover_item(self, arquivo, lista, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um item para remover.")
            return
        for item in selecionado:
            valores = tree.item(item, "values")
            lista.remove(list(valores))
            tree.delete(item)
        self.salvar_dados(arquivo, lista)
    
    def abrir_janela_novo(self, arquivo, lista, tree, campos):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Adicionar Novo Registro")
        nova_janela.geometry("400x300")
        
        entradas = []
        for campo in campos:
            tk.Label(nova_janela, text=campo + ":").pack(pady=5)
            entry = tk.Entry(nova_janela)
            entry.pack(pady=5)
            entradas.append(entry)
        
        def adicionar():
            novo_item = [entry.get() for entry in entradas]
            lista.append(novo_item)
            tree.insert("", "end", values=novo_item)
            self.salvar_dados(arquivo, lista)
            nova_janela.destroy()
        
        tk.Button(nova_janela, text="Adicionar", command=adicionar).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicativo(root)
    root.mainloop()
