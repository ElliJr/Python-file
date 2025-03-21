import tkinter as tk
from tkinter import ttk, messagebox
import json

class Aplicativo:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento")
        self.root.attributes('-fullscreen', True)
        
        # Cores
        self.cor_principal = "#1E3A5F"  # Azul escuro
        self.cor_secundaria = "#2C5EAA"  # Azul médio
        self.cor_destaque = "#D9A87E"  # Marrom suave
        self.cor_fonte = "white"
        
        self.main_frame = tk.Frame(root, bg=self.cor_principal)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.sidebar = tk.Frame(self.main_frame, bg=self.cor_secundaria, width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        self.content_frame = tk.Frame(self.main_frame, bg="white")
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.paginas = {}
        
        botoes = ["Financeiro", "Vendas", "Compras", "Clientes", "Produtos", "Relatórios", "Configurações", "Suporte"]
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
        for nome in ["Financeiro", "Vendas", "Compras", "Clientes", "Produtos", "Relatórios", "Configurações", "Suporte"]:
            frame = tk.Frame(self.content_frame, bg="white")
            label = tk.Label(frame, text=nome, font=("Arial", 24), bg="white")
            label.pack(pady=20)
            self.paginas[nome] = frame
        
        self.criar_pagina_produtos()
        self.criar_pagina_clientes()
    
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
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicativo(root)
    root.mainloop()
