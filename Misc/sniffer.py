###
# Python 3  -  Raspian - Raw Socket interface
###

import socket
import os
import math

def sniffing(host, win, socket_prot):
    "sniffing(host_ip_address, operating_system_is_windows, socket_protocol)"
    while 1:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_prot)
        sniffer.bind((host, 0))
        # include the IP headers in the captured packets
        
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if win == 1:  # if windows
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        # read in a single packet
        a = sniffer.recvfrom(65565)
        print("test")
        return a
    
 

if __name__ == '__main__':
    HOST = '192.168.1.224'
    
    sniffed, ipaddr = sniffing(HOST,0,socket.IPPROTO_UDP)

    print("__main__.decode_packet()")
    

    xx="0x"+"".join(["{:02x}".format(sniffed[x]) for x in range(len(sniffed))])
    print(xx)
##    d = decode_packet()
##    print("Decode packet:\n",d)
##    port = d["UDP Source_Port"].to_bytes(2, "big")
##    print("UDP Source_Port",port)
##    address = bytes2address(port+d["IPv4 Source_Address"].to_bytes(4, "big"))
