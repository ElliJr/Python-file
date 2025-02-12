import winsound
import os
import time

# Pegando entrada do usuário e convertendo para inteiro


os.system("color a")  
print("\n🚨 ERRO FATAL DETECTADO 🚨")
time.sleep(2)

    # Beeps assustadores
for _ in range(5):
    winsound.Beep(500, 300)
    time.sleep(0.5)

    print("\n🔴 ALERTA: Um vírus foi detectado no sistema 🔴")
    time.sleep(2)

    print("\n💣 Iniciando eliminação de arquivos...")
    time.sleep(1)

    # Contagem regressiva falsa
    for i in range(5, 0, -1):
        print(f"💀 Deletando System32 em {i} segundos...")
        winsound.Beep(700, 300)
        time.sleep(1)

    print("\n💀 ERRO 404: O Windows falhou miseravelmente 💀")
    time.sleep(2)

    # Abre o CMD em tela cheia, muda a cor para vermelho e exibe uma mensagem assustadora
    os.system('start cmd /k "mode con: cols=1000 lines=500 & color a & title ERRO FATAL & echo VOCÊ NÃO DEVERIA TER JOGADO ESSE JOGO..."')

    # Abre outra janela do CMD piscando na tela
    for _ in range(3):
        os.system("start cmd /k mode con: cols=1000 lines=500 & color a & title ALERTA")
        time.sleep(1)

    # Executa um comando no CMD para exibir mensagens infinitas
    os.system('start cmd /k "mode con: cols=1000 lines=500 & color a & for /L %i in (1,0,2) do echo SYSTEM ERROR DETECTED!!!"')
    break
