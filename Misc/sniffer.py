###
# Python 3  -  Raspian - Raw Socket interface
###

import socket
import os
import math
import construct_IPv4_header2 as construct

def sniffing(host, win, socket_prot):
    "sniffing(host_ip_address, operating_system_is_windows, socket_protocol)"
    while 1:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_prot)
        sniffer.bind((host, 0))
        # include the IP headers in the captured packets
        
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        print("test")
        if win == 1:  # if windows
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        # read in a single packet
        a = sniffer.recvfrom(65565)
        return a
    
def getfield(intrep,headerlen,length=4,offset=4):     
        return ((intrep<<offset)%pow(2,headerlen))>>(headerlen-length)

if __name__ == '__main__':
    HOST = '192.168.1.225'
    print("Start Main")
    sniffed, ipaddr = sniffing(HOST,0,socket.IPPROTO_UDP)

    print("__main__.decode_packet()")
    

    xx="0x"+"".join(["{:02x}".format(sniffed[x]) for x in range(len(sniffed))])
    print(xx)
    
    IPv4_sniff = int(xx[0:40],16)
    UDP_sniff = int(xx[40:48],16)
    msg_sniff = int(xx[48:],16)
    
    IPv4 = construct.construct_IPv4_header()
    UDP = construct.construct_UDP_header()
    
    for f in IPv4.field_name_list:

        bit_offset = getattr(IPv4,f).bit_offset
        bit_length = getattr(IPv4,f).bit_length
        
##        WF_field_format="{{:20s}}: 0{1:}{{:0{0:}{1:}}}".format(
##            *(bit_length,"b") if bit_length%4 else (bit_length//4,"x"))
        WF_field_format = "{:20s}: {:d}"
        WF_field_value = getfield(IPv4_sniff,160,offset=bit_offset,length=bit_length)
        print(WF_field_format.format(f,getfield(IPv4_sniff,160,offset=bit_offset,length=bit_length)))
    
    for f in UDP.field_name_list:

        bit_offset = getattr(UDP,f).bit_offset
        bit_length = getattr(UDP,f).bit_length
        
##        WF_field_format="{{:20s}}: 0{1:}{{:0{0:}{1:}}}".format(
##            *(bit_length,"b") if bit_length%4 else (bit_length//4,"x"))
        WF_field_format = "{:20s}: {:d}"
        WF_field_value = getfield(UDP_sniff,32,offset=bit_offset,length=bit_length)
        print(WF_field_format.format(f,getfield(UDP_sniff,32,offset=bit_offset,length=bit_length)))
##    d = decode_packet()
##    print("Decode packet:\n",d)
##    port = d["UDP Source_Port"].to_bytes(2, "big")
##    print("UDP Source_Port",port)
##    address = bytes2address(port+d["IPv4 Source_Address"].to_bytes(4, "big"))
