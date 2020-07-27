import socket
from multiprocessing import Process
def talk(conn):
    try:
        while True:
            conn.send(b'hello')
            print(conn.recv(1024))
    finally:
        conn.close()
if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1',9091))
    sk.listen()
    try:
        while True:
            conn,addr = sk.accept()
            Process(target=talk,args=(conn,)).start()
    finally:
        sk.close()
