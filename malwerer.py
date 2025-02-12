import os
import time

# Mudar a cor do terminal para verde (Linux)
os.system("echo -e '\033[0;32m'")  # Verde

print("\n🚨 ERRO FATAL DETECTADO 🚨")
time.sleep(2)

# Beeps assustadores (usando `echo -e '\a'` para fazer o terminal bipar)
for _ in range(5):
    print("\a")  # Tenta gerar som no terminal
    time.sleep(0.5)

print("\n🔴 ALERTA: Um vírus foi detectado no sistema 🔴")
time.sleep(2)

print("\n💣 Iniciando eliminação de arquivos...")
time.sleep(1)

# Contagem regressiva falsa
for i in range(5, 0, -1):
    print(f"💀 Deletando System32 em {i} segundos...")
    time.sleep(1)

print("\n💀 ERRO 404: O ChromeOS falhou miseravelmente 💀")
time.sleep(2)

# Abrir várias janelas do terminal piscando (Linux)
for _ in range(3):
    os.system("gnome-terminal -- bash -c 'echo ALERTA!! && sleep 2'")
    time.sleep(1)

# Executa um comando para exibir mensagens infinitas no terminal
os.system("gnome-terminal -- bash -c 'while true; do echo SYSTEM ERROR DETECTED!!!; sleep 1; done'")
