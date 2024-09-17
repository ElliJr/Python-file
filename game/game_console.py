import tkinter as tk

# Variáveis globais do jogo
you_life = 1000
emine_life = 1000
you_sword_attack = 999999999
emine_sword_attack = 200

def update_status():
    """Atualiza a exibição de status de vida do jogador e do inimigo."""
    player_life_label.config(text=f"Sua vida: {you_life}")
    enemy_life_label.config(text=f"Vida do inimigo: {emine_life}")
    
def attack():
    """Função para atacar o inimigo diretamente."""
    global emine_life
    emine_life -= you_sword_attack
    status_label.config(text=f"Você atacou e causou {you_sword_attack} de dano!")

    if emine_life <= 0:
        status_label.config(text="Você venceu!")
        disable_buttons()
    else:
        emine_action()
    
    update_status()

def defend():
    """Função para se defender."""
    status_label.config(text="Você se defendeu!")
    emine_action()
    update_status()

def flee():
    """Função para fugir da batalha."""
    status_label.config(text="Você fugiu da batalha!")
    disable_buttons()

def emine_action():
    """Função para a ação do inimigo."""
    global you_life
    you_life -= emine_sword_attack
    status_label.config(text=f"O inimigo atacou e causou {emine_sword_attack} de dano!")

    if you_life <= 0:
        status_label.config(text="Você foi derrotado!")
        disable_buttons()

    update_status()

def disable_buttons():
    """Desativa os botões de ação quando o jogo termina."""
    attack_button.config(state=tk.DISABLED)
    defend_button.config(state=tk.DISABLED)
    flee_button.config(state=tk.DISABLED)

# Configuração da janela principal do tkinter
root = tk.Tk()
root.title("Jogo de RPG")
root.geometry("250x170")

# Labels de status
player_life_label = tk.Label(root,text=f"Sua vida: {you_life}")
player_life_label.pack()

enemy_life_label = tk.Label(root, text=f"Vida do inimigo: {emine_life}")
enemy_life_label.pack()

status_label = tk.Label(root, text="Escolha uma ação")
status_label.pack()

# Botões de ação
attack_button = tk.Button(root, text="Atacar", command=attack)
attack_button.pack()

defend_button = tk.Button(root, text="Defender", command=defend)
defend_button.pack()

flee_button = tk.Button(root, text="Fugir", command=flee)
flee_button.pack()

# Atualiza a interface inicialmente
update_status()

# Inicia o loop principal da interface
root.mainloop()
