import os
import tkinter as tk
from tkinter import ttk
from pygame import mixer
import threading

class TwiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Twice 🎵")
        self.root.geometry("800x400")
        self.root.configure(bg="#252525")  # Fundo cinza escuro

        # Inicializando mixer
        mixer.init()

        self.current_song_index = 0
        self.is_paused = False
        self.is_repeating = False

        self.song_list = []

        # Barra de progresso
        self.progress_frame = tk.Frame(root, bg="#252525")
        self.progress_frame.pack(pady=5, fill="x")

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Scale(
            self.progress_frame,
            from_=0,
            to=100,
            orient="horizontal",
            variable=self.progress_var,
            command=self.seek_song
        )
        self.progress_bar.pack(fill="x", padx=10, pady=2)

        self.time_label = tk.Label(self.progress_frame, text="00:00 / 00:00", bg="#252525", fg="white", font=("Arial", 10))
        self.time_label.pack()

        # Container principal
        self.main_frame = tk.Frame(root, bg="#252525")
        self.main_frame.pack(fill="both", expand=True)

        # Container para músicas com rolagem
        self.canvas = tk.Canvas(self.main_frame, bg="#2E2E2E")
        self.canvas.pack(side="left", pady=10, fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="left", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.song_frame = tk.Frame(self.canvas, bg="#2E2E2E")
        self.canvas.create_window((0, 0), window=self.song_frame, anchor="nw")

        self.song_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Adicionar suporte ao scroll com o mouse
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Card de música atual
        self.current_song_frame = tk.Frame(self.main_frame, bg="#3C3C3C", bd=2, relief="solid")
        self.current_song_frame.pack(side="right", fill="y", padx=10, pady=10)

        self.current_song_label = tk.Label(
            self.current_song_frame,
            text="Nenhuma música tocando",
            font=("Arial", 14, "bold"),
            bg="#3C3C3C",
            fg="white",
            wraplength=200,
            justify="center"
        )
        self.current_song_label.pack(padx=10, pady=20)

        # Botões de controle
        control_frame = tk.Frame(root, bg="#3C3C3C", bd=2, relief="solid")  # Fundo diferente para os controles
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="⏮️ Anterior", command=self.prev_song, bg="#FF8C00", fg="white", width=10).grid(row=0, column=0, padx=5)
        tk.Button(control_frame, text="▶️ Play", command=self.play_song, bg="#FF8C00", fg="white", width=10).grid(row=0, column=1, padx=5)
        tk.Button(control_frame, text="⏸️ Pause", command=self.pause_song, bg="#FF8C00", fg="white", width=10).grid(row=0, column=2, padx=5)
        tk.Button(control_frame, text="⏹️ Stop", command=self.stop_song, bg="#FF8C00", fg="white", width=10).grid(row=0, column=3, padx=5)
        tk.Button(control_frame, text="⏭️ Próximo", command=self.next_song, bg="#FF8C00", fg="white", width=10).grid(row=0, column=4, padx=5)

        tk.Button(root, text="🔄 Repetir Música", command=self.toggle_repeat, bg="#FF8C00", fg="white").pack(pady=5)

        volume_frame = tk.Frame(root, bg="#3C3C3C", bd=2, relief="solid")  # Fundo diferente para o controle de volume
        volume_frame.pack(pady=10)

        tk.Button(volume_frame, text="🔉 Volume -", command=self.decrease_volume, bg="#FF8C00", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(volume_frame, text="🔊 Volume +", command=self.increase_volume, bg="#FF8C00", fg="white").grid(row=0, column=1, padx=5)

        # Iniciar thread de atualização de progresso
        self.running = True
        threading.Thread(target=self.update_progress, daemon=True).start()

        # Carregar músicas ao iniciar
        self.load_songs_from_memes_folder()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def load_songs_from_memes_folder(self):
        # Caminho para a pasta de músicas "memes" no diretório atual
        current_directory = os.path.dirname(os.path.realpath(__file__))  # Diretório onde o script está
        memes_folder = os.path.join(current_directory, "memes")

        if os.path.exists(memes_folder):
            # Carrega todos os arquivos mp3 e wav da pasta memes
            self.song_list = [os.path.join(memes_folder, f) for f in os.listdir(memes_folder) if f.endswith((".mp3", ".wav"))]
            if self.song_list:
                self.update_song_display()
            else:
                self.show_error("Não há músicas na pasta memes!")
        else:
            self.show_error("A pasta 'memes' não foi encontrada!")

    def update_song_display(self):
        # Limpa a área de exibição antes de adicionar
        for widget in self.song_frame.winfo_children():
            widget.destroy()

        # Exibe os botões das músicas lado a lado
        for index, song in enumerate(self.song_list):
            song_name = os.path.basename(song)
            song_button = tk.Button(self.song_frame, text=song_name, command=lambda i=index: self.play_song(i), bg="#FF8C00", fg="white")
            song_button.grid(row=index // 5, column=index % 5, padx=5, pady=5)  # Organiza em colunas e linhas

    def show_error(self, message):
        # Exibe um erro na interface
        error_label = tk.Label(self.root, text=message, fg="red", bg="#2E2E2E", font=("Arial", 12))
        error_label.pack(pady=5)

    def play_song(self, index=None):
        if index is not None:
            self.current_song_index = index
        song_path = self.song_list[self.current_song_index]
        mixer.music.load(song_path)
        mixer.music.play()

        # Atualiza o card de música atual
        current_song_name = os.path.basename(song_path)
        self.current_song_label.config(text=f"Tocando agora:\n{current_song_name}")

        self.update_song_display()

    def pause_song(self):
        if not self.is_paused:
            mixer.music.pause()
            self.is_paused = True
        else:
            mixer.music.unpause()
            self.is_paused = False

    def stop_song(self):
        mixer.music.stop()
        self.is_paused = False

    def prev_song(self):
        self.current_song_index = (self.current_song_index - 1) % len(self.song_list)
        self.play_song()

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.song_list)
        self.play_song()

    def toggle_repeat(self):
        self.is_repeating = not self.is_repeating

    def increase_volume(self):
        current_volume = mixer.music.get_volume()
        mixer.music.set_volume(min(1.0, current_volume + 0.1))

    def decrease_volume(self):
        current_volume = mixer.music.get_volume()
        mixer.music.set_volume(max(0.0, current_volume - 0.1))

    def update_progress(self):
        while self.running:
            if mixer.music.get_busy():
                current_time = mixer.music.get_pos() // 1000
                total_length = self.get_song_length()
                if total_length > 0:
                    self.progress_var.set((current_time / total_length) * 100)

                self.time_label.config(
                    text=f"{self.format_time(current_time)} / {self.format_time(total_length)}"
                )
            threading.Event().wait(1)  # Reduz a carga com espera de 1 segundo

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def get_song_length(self):
        try:
            return int(mixer.Sound(self.song_list[self.current_song_index]).get_length())
        except Exception:
            return 0

    def seek_song(self, value):
        total_length = self.get_song_length()
        seek_time = (float(value) / 100) * total_length
        mixer.music.play(start=seek_time)

# Executar a aplicação
root = tk.Tk()
app = TwiceApp(root)
root.mainloop()