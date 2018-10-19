# OSocket
#
import socket.socket as oldsock

rpc2xx = {
        "INIT":     bytes([0,0]),
        "BIND":     bytes([1,0]),
        "SENDTO":   bytes([2,0]),
        "RECVFROM": bytes([3,0]),
        "CLOSE":    bytes([4,0])
        }

xx2rpc = {v:k for v,k in opcodes2bin.items()}

class RPC_API_socket:pass
    
class RPC_HANDER_socket:
    
    def __init__(self,af=2,sock=2):
        
        if af != 2 or sock !=2:
            raise ValueError("Only Socket(2,2) is supported")
        
    def __enter__(self):
        
        self.ipc = socket.socket(2,2)
        self.ipc.sendto(START,upaddr2bytes("127.0.0.1",4000))
        msg,address = self.ipc.recvfrom(2000)
        
        return self
    
    def __exit__(self,a,b,c):
        
        self.ipc.sendto(("127.0.0.1",4000))
        self.fd.close()
        
        return a==b==c==None
                           
    def bytes2address(self,X):
        if len(X)!=6:
            raise ValueError("ipc header len not 6")
        return (".".join([str(x) for x in X[2:]]),int.from_bytes(X[:2],"big"))
            
    def address2bytes(self,address):
        if not all(
            [type(address) is tuple,
             len(address) == 2,
             type(address[0]) is str,
             type(address[1]) is int,
             all([0<=int(digit256)<256 for digit256 in address[0].split(".")]),
             0<address[1]<65536]
            ):raise ValueError("Invalid address {}".format(address))

        return bytes(list(divmod(address[1],256))+[
            int(digit256) for digit256 in address[0].split(".")])
                         
    def bind(self,address):
        
        self.send_to(BIND,address)

