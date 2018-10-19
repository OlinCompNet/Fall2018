
import InternetWireFormat
IFW=InternetWireFormat.Internet_Wire_Format
from Nat import Nat
def construct_IPv4_header():

    with IFW() as IPv4:
        IPv4.boundary(32) # Set boundary. 
                          # IETF headers are usually assumed to begin on
                          # a bit address that is a multiple of 2**32
        IPv4.Version = field("Version",4,Nat,4)
        IPv4.INL = field("IHL",0,Nat,4) 
        IPv4.Type_of_Service = field("Type of Service",0,Nat,8)
        IPv4.Total_Length = field("Total Length",0,Nat,16)
        IPv4.Identification = field("Identification",0,Nat,16)
        IPv4.Flags = field("Flags",0,Nat,3)
        IPv4.Fragment_Offset = field("Fragment Offset",0,Nat,16)
        IPv4.Time_to_Live = field("Time to Live",0,Nat,8)
        IPv4.Protocol = field("Protocol",0,Nat,8)
        IPv4.Header_Checksum = field("Header Checksum",0,Nat,16)
        IPv4.Source_Address = field("Source Address",0,Nat,16) # (0-15)
        IPv4.Destination_Address = field("Destination Address",1,Nat,16) # (16-31)
        IPv4.Options = field("Options",0,Nat,24)
        IPv4.Padding = field("Padding",0,Nat,8)

        IPv4.boundary(32)
    return IPv4
if __name__ == "__main__":
    
#    IPv4 = construct_IPv4_header()
#    print(IPv4)
##
##print("Test parsing")                       
##                   
    IPv4_eg = 0x4500005441e040004001e4c00a0000040a000005
##
##ParsedHeader = IPv4.parse(IPv4_eg))
##print(ParsedHeader)
##    
    
