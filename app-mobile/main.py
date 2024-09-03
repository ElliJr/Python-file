from kivy.app import App
from kivy.lang import Builder

GUI: object = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GU
