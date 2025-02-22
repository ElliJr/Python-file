import tkinter as tk
from tkinter import messagebox
import random

# Dados dos Pokémon iniciais
pokemon_data = {
    "Charmander": {"HP": 39, "Ataques": {"Arranhão": 10, "Brasa": 15}},
    "Squirtle": {"HP": 44, "Ataques": {"Investida": 10, "Jato d'Água": 15}},
    "Bulbasaur": {"HP": 45, "Ataques": {"Chicote de Vinha": 12, "Investida": 10}}
}

class PokemonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Adventure")
        self.root.geometry("500x400")

        # Inicializa variáveis do jogo
        self.player_name = ""
        self.player_pokemon = None
        self.pokemon_hp = 0
        self.wild_pokemon = None
        self.wild_hp = 0

        self.main_menu()

    def main_menu(self):
        """Tela inicial do jogo."""
        self.clear_window()

        tk.Label(self.root, text="Bem-vindo ao mundo Pokémon!", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Digite seu nome:").pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Button(self.root, text="Avançar", command=self.choose_pokemon).pack(pady=10)

    def choose_pokemon(self):
        """Escolha do Pokémon inicial."""
        self.player_name = self.name_entry.get().strip().title()

        if not self.player_name:
            messagebox.showwarning("Erro", "Por favor, digite um nome válido.")
            return

        self.clear_window()
        tk.Label(self.root, text=f"Olá {self.player_name}, escolha seu Pokémon!", font=("Arial", 14)).pack(pady=10)

        for pkm in pokemon_data.keys():
            tk.Button(self.root, text=pkm, command=lambda p=pkm: self.start_game(p)).pack(pady=5)

    def start_game(self, pokemon):
        """Inicia o jogo com o Pokémon escolhido."""
        self.player_pokemon = pokemon
        self.pokemon_hp = pokemon_data[pokemon]["HP"]

        self.clear_window()
        tk.Label(self.root, text=f"{self.player_name}, você escolheu {self.player_pokemon}!", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Explorar", command=self.explore).pack(pady=10)

    def explore(self):
        """Exploração do mundo Pokémon, onde podem surgir batalhas aleatórias."""
        self.clear_window()
        tk.Label(self.root, text="Você está explorando...", font=("Arial", 14)).pack(pady=10)

        if random.random() < 0.5:
            self.battle()
        else:
            tk.Label(self.root, text="Nenhum Pokémon apareceu.").pack()
            tk.Button(self.root, text="Continuar explorando", command=self.explore).pack(pady=10)

    def battle(self):
        """Inicia uma batalha contra um Pokémon selvagem."""
        self.wild_pokemon = random.choice(list(pokemon_data.keys()))
        self.wild_hp = pokemon_data[self.wild_pokemon]["HP"]

        self.clear_window()
        tk.Label(self.root, text=f"🔥 Um {self.wild_pokemon} selvagem apareceu! 🔥", font=("Arial", 14)).pack(pady=10)

        # Exibir HP do jogador e do Pokémon selvagem
        self.player_hp_label = tk.Label(self.root, text=f"{self.player_pokemon} HP: {self.pokemon_hp}")
        self.player_hp_label.pack()
        
        self.wild_hp_label = tk.Label(self.root, text=f"{self.wild_pokemon} HP: {self.wild_hp}")
        self.wild_hp_label.pack()

        # Criar botões de ataque
        for attack, damage in pokemon_data[self.player_pokemon]["Ataques"].items():
            tk.Button(self.root, text=attack, command=lambda a=attack, d=damage: self.attack(a, d)).pack(pady=5)

    def attack(self, attack_name, damage):
        """O jogador ataca o Pokémon selvagem."""
        self.wild_hp -= damage
        self.wild_hp_label.config(text=f"{self.wild_pokemon} HP: {self.wild_hp}")

        messagebox.showinfo("Ataque!", f"Seu {self.player_pokemon} usou {attack_name}! Causou {damage} de dano!")

        if self.wild_hp <= 0:
            messagebox.showinfo("Vitória!", f"Você derrotou {self.wild_pokemon}!")
            self.explore()
        else:
            self.enemy_attack()

    def enemy_attack(self):
        """O Pokémon selvagem ataca o jogador."""
        enemy_attack_name, enemy_damage = random.choice(list(pokemon_data[self.wild_pokemon]["Ataques"].items()))
        self.pokemon_hp -= enemy_damage
        self.player_hp_label.config(text=f"{self.player_pokemon} HP: {self.pokemon_hp}")

        messagebox.showinfo("Contra-ataque!", f"{self.wild_pokemon} usou {enemy_attack_name}! Causou {enemy_damage} de dano!")

        if self.pokemon_hp <= 0:
            messagebox.showinfo("Derrota!", "Seu Pokémon ficou sem energia...")
            self.main_menu()
        else:
            self.battle()  # Continua a batalha

    def clear_window(self):
        """Remove todos os widgets da janela."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = PokemonGame(root)
    root.mainloop()
