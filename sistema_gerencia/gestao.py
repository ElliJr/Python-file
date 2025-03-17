import tkinter as tk
from tkinter import ttk, messagebox
import json

class Aplicativo:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento")
        self.root.attributes('-fullscreen', True)
        
        self.main_frame = tk.Frame(root, bg="#F8F9FA")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.sidebar = tk.Frame(self.main_frame, bg="#2D3E50", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        botoes = ["Financeiro", "Vendas", "Compras", "Clientes", "Produtos", "Relatórios", "Configurações", "Suporte"]
        for btn in botoes:
            tk.Button(self.sidebar, text=btn, bg="#2D3E50", fg="white", font=("Arial", 12), bd=0, relief="flat", 
                      activebackground="#1B2B3A", padx=10, pady=5, anchor='w').pack(fill=tk.X)
        
        self.header = tk.Frame(self.main_frame, bg="#E9ECEF", height=50)
        self.header.pack(fill=tk.X)
        
        self.search_entry = tk.Entry(self.header, font=("Arial", 12), width=40)
        self.search_entry.pack(pady=10, padx=20, side=tk.LEFT)
        
        tk.Button(self.header, text="🔍", font=("Arial", 12), command=self.pesquisar).pack(pady=10, side=tk.LEFT)
        
        self.content_frame = tk.Frame(self.main_frame, bg="white")
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.tab_control = ttk.Notebook(self.content_frame)
        self.tab_produtos = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_produtos, text="Produtos")
        self.tab_control.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(self.tab_produtos, columns=("#1", "#2", "#3", "#4", "#5"), show="headings")
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
        
        self.secao_botoes = tk.Frame(self.tab_produtos, bg="white")
        self.secao_botoes.pack(pady=10)
        
        self.btn_novo = tk.Button(self.secao_botoes, text="+ Novo", font=("Arial", 12), bg="#4CAF50", fg="white", 
                                  command=self.abrir_janela_novo_produto)
        self.btn_novo.grid(row=0, column=0, padx=10, pady=10)
        
        self.botao_remover = tk.Button(self.secao_botoes, text="Remover Tipo", font=("Arial", 14), bg="#F44336", fg="white", 
                                       activebackground="#e53935", command=self.remover_tipo, relief="raised")
        self.botao_remover.grid(row=0, column=1, padx=10, pady=10)
        
        self.produtos = []
        self.carregar_produtos()
        
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
        
        tk.Label(nova_janela, text="Nome do Produto:").pack(pady=5)
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
    
    def pesquisar(self):
        termo = self.search_entry.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for produto in self.produtos:
            if termo in str(produto[1]).lower():
                self.tree.insert("", "end", values=produto)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicativo(root)
    root.mainloop()
