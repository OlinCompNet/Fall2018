# bytes2address translate binary ip address and port number to python "address"
# note this is the application programming iterface kit for UDP.
# to send down the stack the application uses
#   fd.sendto(msg,address)
#   the address is decoded to 6 bytes by address2bytes
#   these six bytes are broken into:
#   port: 2 bytes
#   ipaddress: 4 bytes.
#  the remainder of the packet is the message in bytes (not in unicode)
#       
# to receive up the stack the application uses
# msg, address = fd.recvfrom(bufferlength)
#
# recvfrom parses the first six bytes as
# 2 bytes - port
# 4 bytes - IPv4 address 
#  
#   
#   bytes2address header (port+ipaddress)
#   


# 
# 
# 
#   
#
# 



def bytes2address(X):
    if len(X)!=6:
         raise ValueError("ipc header len not 6")
    return (".".join([str(x) for x in X[2:]]),int.from_bytes(X[:2],"big"))
def address2bytes(address):
    if not all(
        [type(address) is tuple,
         len(address) == 2,
         type(address[0]) is str,
         type(address[1]) is int,
         all([0<=int(digit256)<256 for digit256 in address[0].split(".")]),
         0<address[1]<65536]
        ):
        raise ValueError("Invalid address {}".format(address))

    return bytes(list(divmod(address[1],256))+[
        int(digit256) for digit256 in address[0].split(".")])

                         
if __name__ == "__main__":
    address = ("192.168.1.10",4440)
    a2b = address2bytes(address)
    print(a2b)
    b2a = bytes2address(a2b)
    print(b2a)
    
    
                      
                
