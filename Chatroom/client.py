from socket import *
from threading import Thread

def recieve():
    while True:
        msg = client_socket.recv(1024).decode("utf8")
        print(msg)

def send():
    while True:
        msg = input()
        client_socket.send(bytes(msg,"utf8"))


ADDR = ('192.168.1.225', 5000)

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=recieve)
send_thread = Thread(target=send)
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()
