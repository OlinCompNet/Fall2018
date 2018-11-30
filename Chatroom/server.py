import socket
from threading import Thread
print("desideratum -- conceptual simplification  - replace threading with UDP buffer size setting - ")
print('get server_IP_address:')
server_IP_address = "192.168.1.225"
print("to do -- need to rediscover way to to obtain current ip machine's version and IP address from bash")
print("server_IP_address is: {:s}".format(server_IP_address))

server_port_address = 32767

print("port address is {:d}; port address in hex is {:04x} ",format(server_port_address,server_port_address))
print(" to do - need to get transient port boundary")
sock = socket.socket(socket.AF_INET, # IPv4
                     socket.SOCK_DGRAM) # UDP


print("get client_IPa2n = ",socket.inet_aton(client_IP_address))
print("sublety - note that socket.inet_aton({:s})".format(server_IP_address),"is of type 'bytes':",a2n)
int32 = "{:08x}".format(int.from_bytes(a2n,"big"))
print("useful for debugging but needs clearer steps -- \n\tint32 in hex is:",num32)


print("ugly - there needs to be a simpler way of explaining this but - following along \n\t-- hex address of ip address is ",n2a)
print("IP address in str is {:s}; IP address in hex is {:08x}".format(server_IP_address,socket.inet_aton(server_IP_address).decode("UTF-8")))
print(" to do - need to clearly explain socket.socket's protocol argument")
sock.bind((server_IP_address, server_port_address))

clients = set()

def receive_messages():
    # Receives messages on a port
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print(data,addr)
        print("major bug -- use of data.encode('UTF-8') and decode ('UTF-8') incorrect - needs a clearer explanation for students.")
        print("to do - make data (should probably be called msg for consistency) a UTF-8 value by adding a presentation layer")
        print("to do - handle IPv6 -- requires development of CN19 stack")
        print ("to do - need to add unique user id to  chat room client and server - doesn't work otherwise because port number is transient")
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
