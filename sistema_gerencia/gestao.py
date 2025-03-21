import tkinter as tk
from tkinter import ttk, messagebox
import json

class Aplicativo:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento")
        self.root.geometry("1300x800")
        
        # Cores
        self.cor_principal = "#1E3A5F"  # Azul escuro
        self.cor_secundaria = "#2C5EAA"  # Azul médio
        self.cor_destaque = "#D9A87E"  # Marrom suave
        self.cor_fonte = "white"
        
        self.main_frame = tk.Frame(root, bg=self.cor_principal)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.sidebar = tk.Frame(self.main_frame, bg=self.cor_secundaria, width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        self.content_frame = tk.Frame(self.main_frame, bg="#0e075b")
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.paginas = {}
        
        botoes = ["Financeiro", "Vendas", "Compras", "Clientes", "Produtos", "Relatórios", "Configurações", "Suporte"]
        for btn in botoes:
            tk.Button(self.sidebar, text=btn, bg=self.cor_secundaria, fg=self.cor_fonte, font=("Arial", 12), bd=0, relief="flat", 
                      activebackground=self.cor_destaque, padx=10, pady=5, anchor='w', command=lambda b=btn: self.mudar_pagina(b)).pack(fill=tk.X)
        
        self.criar_paginas()
        self.mudar_pagina("Login")
        
    def criar_paginas(self):
        for nome in ["Financeiro", "Vendas", "Compras", "Clientes", "Produtos", "Relatórios", "Configurações", "Suporte", "Login"]:
            frame = tk.Frame(self.content_frame, bg="#c16e65")
            label = tk.Label(frame, text=nome, font=("Arial", 24), bg="white")
            label.pack(pady=20)
            self.paginas[nome] = frame
            
        self.criar_pagina_produtos()
        
    def criar_pagina_produtos(self):
        frame = self.paginas["Produtos"]
        
        self.tree = ttk.Treeview(frame, columns=("#1", "#2", "#3", "#4", "#5"), show="headings")
        self.tree.heading("#1", text="Cód")
        self.tree.heading("#2", text="Produto")
        self.tree.heading("#3", text="Categoria")
        self.tree.heading("#4", text="Preço Venda")
        self.tree.heading("#5", text="Estoque")
        
        self.tree.column("#1", width=50, anchor="center")
        self.tree.column("#2", width=200, anchor="w")
        self.tree.column("#3", width=150, anchor="w")
        self.tree.column("#4", width=100, anchor="center")
        self.tree.column("#5", width=80, anchor="center")
        
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.secao_botoes = tk.Frame(frame, bg="white")
        self.secao_botoes.pack(pady=10)
        
        self.btn_novo = tk.Button(self.secao_botoes, text="+ Novo", font=("Arial", 12), bg=self.cor_secundaria, fg=self.cor_fonte, 
                                  command=self.abrir_janela_novo_produto)
        self.btn_novo.grid(row=0, column=0, padx=10, pady=10)
        
        self.botao_remover = tk.Button(self.secao_botoes, text="Remover Tipo", font=("Arial", 14), bg=self.cor_secundaria, fg=self.cor_fonte, 
                                       activebackground="#e53935", command=self.remover_tipo, relief="raised")
        self.botao_remover.grid(row=0, column=1, padx=10, pady=10)
        
        self.produtos = []
        self.carregar_produtos()
        
    def mudar_pagina(self, pagina):
        for frame in self.paginas.values():
            frame.pack_forget()
        
        self.paginas[pagina].pack(fill=tk.BOTH, expand=True)
        
    def carregar_produtos(self):
        try:
            with open("produtos.json", "r") as file:
                self.produtos = json.load(file)
                for produto in self.produtos:
                    self.tree.insert("", "end", values=produto)
        except FileNotFoundError:
            self.produtos = []
    
    def salvar_produtos(self):
        with open("produtos.json", "w") as file:
            json.dump(self.produtos, file, indent=4)
    
    def remover_tipo(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um item para remover.")
            return
        
        for item in selecionado:
            valores = self.tree.item(item, "values")
            self.produtos = [p for p in self.produtos if p != list(valores)]
            self.tree.delete(item)
        
        self.salvar_produtos()
    
    def abrir_janela_novo_produto(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Adicionar Novo Produto")
        nova_janela.geometry("400x300")
        
        tk.Label(nova_janela,text="Nome do Produto:").pack(pady=5)
        entry_nome = tk.Entry(nova_janela)
        entry_nome.pack(pady=5)
        
        tk.Label(nova_janela, text="Categoria:").pack(pady=5)
        entry_categoria = tk.Entry(nova_janela)
        entry_categoria.pack(pady=5)
        
        tk.Label(nova_janela, text="Preço:").pack(pady=5)
        entry_preco = tk.Entry(nova_janela)
        entry_preco.pack(pady=5)
        
        tk.Label(nova_janela, text="Estoque:").pack(pady=5)
        entry_estoque = tk.Entry(nova_janela)
        entry_estoque.pack(pady=5)
        
        def adicionar():
            novo_produto = [len(self.produtos) + 1, entry_nome.get(), entry_categoria.get(), entry_preco.get(), entry_estoque.get()]
            self.produtos.append(novo_produto)
            self.tree.insert("", "end", values=novo_produto)
            self.salvar_produtos()
            nova_janela.destroy()
        
        tk.Button(nova_janela, text="Adicionar", command=adicionar).pack(pady=10)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicativo(root)
    root.mainloop()
