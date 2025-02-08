from pytube import YouTube
import os

def baixar_video(link):
    try:
        # Cria um objeto YouTube com o link fornecido
        yt = YouTube(link)
        
        # Obtém o stream de maior resolução que é progressivo (vídeo + áudio)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        
        # Confirma se o stream foi encontrado
        if not stream:
            print("Não foi possível encontrar um vídeo compatível para download.")
            return

        # Exibe informações sobre o vídeo
        print(f"Baixando: {yt.title}")
        print(f"Resolução: {stream.resolution}")

        # Define o caminho para salvar o arquivo (opcionalmente, pode ser alterado)
        destino = os.path.expanduser("~/Downloads")  # Baixa na pasta Downloads
        stream.download(output_path=destino)
        
        print(f"Download concluído! O vídeo foi salvo em {destino}")
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    link = input("Digite o link do vídeo do YouTube: ")
    baixar_video(link)
