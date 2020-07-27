import socket
import os

sk = socket.socket()
sk.connect(('127.0.0.1',9091))

while True:
    print(sk.recv(1024))
    sk.send(str(os.getpid()).encode('utf-8'))

