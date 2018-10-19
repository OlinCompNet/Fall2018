#
from InternetWireFormat import Internet_Wire_Format
from Nat import Nat

def construct_UDP_header():
    
    with Internet_Wire_Format() as UDP:
        UDP.boundary(32) # Set boundary.
                         # IETF headers are usually assumed to begin on
                         # a bit address that is a multiple of 2**32
        
        UDP.field("Source Port",0,Nat,16) # (0-15)
        UDP.field("Destination Port",1,Nat,16) # (16-31)
        UDP.field("Length",2,Nat,16) # (32-47) and
        UDP.field("Checksum",3,Nat,16) # (48-63)
        UDP.field("data_octets",4,Nat,64)

        UDP.boundary(32)  # this could be the basis for an attack exercise 
    return UDP

# The field method Pythonicly converts spaces in field names to underbars
UDP = construct_UDP_header()
UDP.data_octets.data_value = 123456
UDP.Source_Port.data_value=0x11
UDP.Destination_Port.data_value=5280 # Layer4.TransientPort()
UDP.Length = UDP.data_octets.data_value.bit_length()
print(UDP)
##    UDP.NextProtocolValue = 33
##    print(UDP_Header.NextProtocol)
##    
    
print("implementation version 2.py")
     
  
