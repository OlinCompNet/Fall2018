
import InternetWireFormat
from InternetWireFormat import Internet_Wire_Format as IWF
from Nat import Nat
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
if __name__ == "__main__":
    IPv4 = construct_IPv4_header()
    print(IPv4)
    IPv4_eg = 0x4500005441e040004001e4c00a0000040a000005
    def getfield(intrep=IPv4_eg,length=4,offset=4,headerlen=160):
        return ((intrep<<offset)%pow(2,headerlen))>>(headerlen-length)
                                                    
    for f in IPv4.field_name_list:
        bit_offset = getattr(IPv4,f).bit_offset
        bit_length = getattr(IPv4,f).bit_length
        
##        WF_field_format="{{:20s}}: 0{1:}{{:0{0:}{1:}}}".format(
##            *(bit_length,"b") if bit_length%4 else (bit_length//4,"x"))
        WF_field_format = "{:20s}: {:d}"
        WF_field_value = getfield(offset=bit_offset,length=bit_length)
        print(WF_field_format.format(f,getfield(offset=bit_offset,length=bit_length)))
        



        
        
    
        

	

    

    
