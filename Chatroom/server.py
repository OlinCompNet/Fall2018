import socket
from threading import Thread

UDP_IP = "127.0.0.1"
UDP_PORT = 5000
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

clients = set()

def receive_messages():
    # Receives messages on a port
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        # if the client is not currently connected, add it to clients
        if addr not in clients:
            clients.add(addr)
            print("connected to:", addr)

        # if client sends 'quit', then disconnect
        if data.decode('UTF8') == 'quit':
            clients.remove(addr)
            print(addr, "deconnected")
        # otherwise, re-broadcast message
        else:
            print("received message:", data.decode('UTF8'), "from", addr)
            # Send out message to other clients
            for client in clients:
                # Exclude the original client address
                if client != addr:
                    sock.sendto(data, client)


t = Thread(target=receive_messages)
t.start()
