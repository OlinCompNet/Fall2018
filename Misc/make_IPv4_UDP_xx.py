import InternetWireFormat
from InternetWireFormat import Internet_Wire_Format as IWF
from Nat import Nat
import socket
import os
import math
TRACING = 1
from bytes2address import *


def sniffing(host, win, socket_prot):
    while 1:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_prot)
        sniffer.bind((host, 0))

        # include the IP headers in the captured packets
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if win == 1:
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        # read in a single packet
        a = sniffer.recvfrom(65565)
        return a



def construct_IPv4_header():
    with IWF() as IPv4:
        IPv4.boundary(32) # Set starting point memory alignment boundary"
        
        IPv4.field("Version",4,Nat,4)
        IPv4.field("IHL",0,Nat,4) 
        IPv4.field("Type of Service",0,Nat,8)
        IPv4.field("Total Length",0,Nat,16)
        IPv4.field("Identification",0,Nat,16)
        IPv4.field("Flags",0,Nat,3)
        IPv4.field("Fragment Offset",0,Nat,13)
        IPv4.field("Time to Live",0,Nat,8)
        IPv4.field("Protocol",0,Nat,8)
        IPv4.field("Header Checksum",0,Nat,16)
        IPv4.field("Source Address",0,Nat,32)  
        IPv4.field("Destination Address",1,Nat,32)  
        IPv4.field("Options",0,Nat,24)
        IPv4.field("Padding",0,Nat,8)
        
        IPv4.boundary(32)
    return IPv4

def construct_UDP_header():
    with IWF() as UDP:
        UDP.boundary(32) # Set starting point memory alignment boundary"
        
        UDP.field("Source Port",4,Nat,16)
        UDP.field("Destination Port",0,Nat,16)
        UDP.field("Length",0,Nat,16)
        UDP.field("Checksum",0,Nat,16)
        
        UDP.boundary(32)
    return UDP

def getfield(intrep=IPv4_eg,headerlen=160,offset=bit_offset,length=bit_length):
    return getfieldn(input_header=intrep,header_length = headerlen, field_offset=offset, field_length = length)
def getfieldn(in_header,header_length,field_length=4,field_offset=4,):
    """get bit field from integer representation of header"""
    return ((in_header<<offset)%pow(2,header_length))>>(header_length-field_length)

def setfield(input_header=0b10101010101010101010,header_length=20,field_length=5,field_offset=3,new_field_value=0b11111):
    """changes field in input_header from bit field_offset to bit field_offset+field_len"""
    ones_mask= ((pow(2,field_length)-1)<<(header_length-field_offset-field_length))
    masked_header = input_header &~ ones_mask
    new_field_value_in_position = new_field_value<<(header_length-field_offset-field_length)
    output_header = masked_header | new_field_value_in_position
    
    if TRACING:
       headerformat  = "{{1:0{0:d}b}} # {{0:s}}".format(header_length)
       print(headerformat.format("input_header",input_header))
       print(headerformat.format("ones_mask",ones_mask))
       print(headerformat.format("masked_header" , masked_header))
       print(headerformat.format("new_field_value_in_position", new_field_value_in_position))
       print(headerformat.format("output_header",output_header))

    return output_header
    

def decode_packet(sniffed = b'E\x00\x00\x1ea\xb8@\x00@\x11\xc4\xc6\n\n\x00 \n\n\x00\x1d\xb5\xc8\x13\x88\x00\n\xb9\xcfhie'):
    print("decode packet")
    IPv4 = construct_IPv4_header()
    UDP = construct_UDP_header()
    IPv4_eg=int.from_bytes(sniffed[:20],"big")
    UDP_eg=int.from_bytes(sniffed[20:28],"big")
    UDP_Data = sniffed[28:]
    dct = {}
    for f in IPv4.field_name_list:
        bit_offset = getattr(IPv4,f).bit_offset
        bit_length = getattr(IPv4,f).bit_length
        dct["IPv4 "+ str(f)] = getfield(intrep=IPv4_eg,headerlen=160,offset=bit_offset,length=bit_length)
        print("IPv4 "+str(f)+": {:}".format(dct["IPv4 "+ str(f)]))
    for g in UDP.field_name_list:
        bit_offset = getattr(UDP,g).bit_offset
        bit_length = getattr(UDP,g).bit_length
        dct["UDP "+ str(g)] = getfield(intrep=UDP_eg,headerlen=64,offset=bit_offset,length=bit_length)
        dct["UDP Data"] = UDP_Data
        print("UDP "+str(g)+": {:}".format(dct["UDP "+str(g)]))
    return dct




def encode_packet(d):
    print("encode_packet")
    IPv4 = construct_IPv4_header()
    UDP = construct_UDP_header()
    
    ipv4_fields = [x.replace(' ','_') for x in ["Version","IHL","Type of Service","Total Length","Identification",
     "Flags","Fragment Offset","Time to Live","Protocol","Header Checksum",
     "Source Address","Destination Address","Options","Padding"]]
    ipv4_fields = IPv4.field_name_list[:]

    udp_fields = [x.replace(' ','_') for x in ["Source Port","Destination Port","Length","Checksum"]]
    udp_fields = UDP.field_name_list[:]
#    ipv4_fields = ["IPv4 "+x.replace(' ', '_') for x in ]
    
#    udp_fields = ["UDP "+x.replace(' ', '_') for x in ]

    fields = ipv4_fields + udp_fields
    print(fields)

    result = d['IPv4 '+ipv4_fields[0]]
    for i in (range(len(ipv4_fields))):
        print(result)
        result = result << getattr(IPv4, ipv4_fields[i]).bit_length
        print(result)
        result = result | d['IPv4 '+ipv4_fields[i]]
        print(result)
        print('\n')

    print("printing UDP fields")
    for i in (range(len(udp_fields))):
        print(udp_fields[i])
        result = result << getattr(UDP, udp_fields[i]).bit_length
        result = result | d['UDP '+udp_fields[i]]
    print(d["UDP Data"],d["UDP Data"])
    data = int.from_bytes(d["UDP Data"], "big")
    result = result << data.bit_length() +1
    result = result | data

    return result.to_bytes(math.ceil(result.bit_length()/8), "big")

if __name__ == '__main__':
    #HOST = '10.10.0.55'
    #decode_packet(sniffed = sniffing(HOST,0,socket.IPPROTO_UDP))
    print("__main__.decode_packet()")
    

    d = decode_packet()
    print(d)
    port = d["UDP Source_Port"].to_bytes(2, "big")
    print("UDP Source_Port",port)
    address = bytes2address(0,port+d["IPv4 Source_Address"].to_bytes(4, "big"))
    print("Address for UDP socket recvfrom",address)

    e = encode_packet(d)
             
    f = decode_packet(e)
    print(f)
    # IPv4 is good, UPD is screwed up (probably off by one error)
