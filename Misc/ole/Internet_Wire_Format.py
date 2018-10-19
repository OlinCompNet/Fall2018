#
# class Internet_Wire_Format
#

import operator
class Octet(bytearray):
    pass

from Nat import Nat

class Internet_Wire_Format:
    
    def __init__(self):
        self.start_wire_format()
        
        
    def __enter__(self):
        return self

    def __exit__(self,a,b,c): 
        return a==b==c==None
    
    def start_wire_format(self):
        self.bit_offset = 0  # bit_offset is current bit pointer into wire format
        self.name_list = []       # order of names in wire format
        self.set_wire_format_memory_bit_alignment()
        self.set_diagram_bit_width()
        return
    def set_wire_format_memory_bit_alignment(self,wire_format_memory_bit_alignment=32):
        "set memory alignment required for wire format "
        if wire_format_memory_bit_alignment not in [32]: # future:... not in [8,16,32,64]:
            raise ValueError("Wire Format bit alignment limited to 32 right now")
        self.wire_format_memory_bit_alignment = wire_format_memory_bit_alignment
    def set_diagram_bit_width(self,diagram_bit_width=32):
        self.diagram_bit_width = diagram_bit_width
        #raise NotImplementedError("for building diagram rulers and numbering bits")
        return

    def set_boundary(self,bit_boundary:Nat)->Nat:
        "move set self.bit_offset to given bit_boundary"
        current_bit_offset = self.bit_offset
        current_bit_offset_boundary = self.bit_offset%bit_boundary #deetermine if already on display_width
        self.bit_offset += 0 if not current_bit_offset else bit_boundary - current_bit_offset
        print("boundary\nbit_offset changed\nfrom {}\nto {}\n".format(current_bit_offset_boundary,self.bit_offset))
        return
    
    def add_field(
        self,
        rfcname=None,
        value=None, #initial value
        data_type=None,
        length=None,
        ):
        name = "_".join(rfcname.split(" "))
        
        if hasattr(self,name): # if object already has field name
            raise ValueError("field name '{}' in use".format(name))
        elif name == None:
            raise ValueError("field name '{}' is not defined")
        else:
            
            print("\nname",name,"\ndata_type",data_type)
            temp = data_type("xxxx",length,self.bit_offset,value)
            setattr(self,
                    name,
                    data_type(
                        name,
                        length,
                        self.bit_offset,
                        value ## what?
                        ))
            
        self.name_list +=[name]  # remember order in which field names were added
        self.bit_offset += length  # bump bit pointer
        print(self.__dir__)
        return len(self.name_list)
    def wire_format_end(self):
        raise NotImplementedError("Not done yet")
    def __str__(self):
        return "\n".join(self.name_list)
            
 
    def __repr__(self):
        print('entering __repr__ of {}'.format(self))
        return """
data_value {}, data_type {}, bit_length {}, bit_offset {} """.format(
    self.data_value,
    self.data_type.__class__.__name__,
    self.bit_length,
    self.bit_offset)
    
if __name__ == "__main__":
    print("Running Unit Test")
    def construct_UDP_header():
    
        with Internet_Wire_Format() as UDP:
            UDP.set_boundary(32) # Set boundary.
                             # IETF headers are usually assumed to begin on
                             # a bit address that is a multiple of 2**32
            
            UDP.add_field("Source Port",997,Nat,16) # (0-15)
            UDP.add_field("Destination Port",998,Nat,16) # (16-31)
            UDP.add_field("Length",999,Nat,16) # (32-47) and
            UDP.add_field("Checksum",1000,Nat,16) # (48-63)
            #UDP.field("data_octets",4,Nat,64)
            UDP.set_boundary(32)
        return UDP
# The field method Pythonicly converts spaces in field names to underbars
    UDP = construct_UDP_header()
    #UDP.data_octets.data_value = 123456
    #print("Source Port",UDP.Source_Port)
    #UDP.Source_Port = 0x1111
    #UDP.Destination_Port.data_value=5280 # Layer4.TransientPort()
    #UDP.Length = UDP.data_octets.data_value.bit_length()
    #print(UDP)
##    UDP.NextProtocolValue = 33
##    print(UDP_Header.NextProtocol)
##    
    print(UDP.Source_Port)
    print(UDP.Destination_Port)
    print(UDP.Length)
    print(UDP.Checksum)
    print("implementation version 2.py")
    
