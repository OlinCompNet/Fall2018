import InternetWireFormat
from InternetWireFormat import Internet_Wire_Format as IWF
from Nat import Nat
print("In L4")

def construct_L4_header():
    with IWF() as L4:
        L4.boundary(8) # Bit Set boundary.
                         # IETF headers are usually assumed to begin on
                         # a bit address that is a multiple of 2**32
        L4.field("Source Port",0,Nat,2) # (0-1)
        L4.field("Destination Port",1,Nat,2) # (2-3)
        L4.field("Length",4,Nat,4) # (4-7) Length of payload
        L4.boundary(8)  # 
    return L4
L4 = construct_L4_header()
L4.Source_Port.data_value=1
L4.Destination_Port.data_value=0 # Layer4.TransientPort()
L4.Length.data_value = 4
print(L4)
