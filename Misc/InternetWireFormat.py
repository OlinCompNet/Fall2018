#
# class InternetWireFormat
#

#import operator
class Octet(bytearray):pass

import Nat
Nat = Nat.Nat

class Internet_Wire_Format:
    
    def __init__(self):
        self.bit_offset = 0  # bit_offset is current bit pointer into header
                             # data structure declaration
        self.field_name_list = []
        
    
               
    def __enter__(self):
        return self

    def __exit__(self,a,b,c): 
        return a==b==c

    def boundary(self,bit_boundary:Nat)->Nat:
        'number of bits in each row from here on'
        "rounds bit counter to next offset"
        #round up to multiple of display width
        current_bit_offset = self.bit_offset%bit_boundary #deetermine if already on display_width
        self.bit_offset += 0 if not current_bit_offset else bit_boundary - current_bit_offset
        return format(self.bit_offset)

    def field(
        self,
        name=None,
        data_value=None,
        data_type=None,
        bit_length=None
        ):
        
        if hasattr(self,name):
            raise ValueError("field name '{}' in use".format(name))
        elif name == None:
            raise ValueError("field name '{}' is not defined")
        
            
        else:
            name = "_".join(name.split(" "))
            setattr(self,name, Field(data_value,data_type,bit_length,self.bit_offset))
        self.field_name_list +=[name]  # remember order in which field names were added
        self.bit_offset += bit_length
    
        return len(self.field_name_list)

    
    def __str__(self):
        return "\n".join(
            ["'{:s}':{:}".format(
                field_name,
                getattr(self,field_name)
                ) for field_name in self.field_name_list])
    

    
class Field:
    def __init__(self, data_value,data_type,bit_length,bit_offset):
        
        self.data_type = data_type
        self.bit_length = bit_length
        self.data_value = data_value
        self.bit_offset = bit_offset

        self.field_element_names = [ # order of field_element_names in __str__
            
            "bit_offset",
            "bit_length",
            "data_type",
            "data_value"
            ]

    def __str__(self):
        print("in __str")
        return "\n"+"\n".join(
            ["\t{:<10}: {:}".format(
                field_element_name,
                getattr(self,field_element_name)
                ) for field_element_name in self.field_element_names])

##    @property
##    def data_value(self):
##        print("IN GETTER FOR data_value")
##        return self.__data_value
##
##    @data_value.setter
##    def data_value(self, data_value):
##        print("IN SETTER FOR data_value")
##        #if not isNat(data_value):
##        #    raise ValueError("argument must be Nat")
##        if not data_value.bit_length() <= self.bit_length:
##            raise ValueError("argument must be <= {}".format(pow(2,self.bit_length)))
##        else:
##            self.__data_value = data_value
##        print("data_value set to ",data_value)
##        return
##
##    def __str__(self):
##        fbn = self.name,
##        fbl = self.bit_length
##        fdt = self.data_type
##        fdv = self.data_value
##        return "{:18} {:5} {:10} {:10}".format(fbn, fbl,fdt,fdv)
##    
##        
##
##    def __repr__(self):
##        return """
##data_value {}, data_type {}, bit_length {}, bit_offset {} """.format(
##    self.data_value,
##    self.data_type.__class__.__name__,
##    self.bit_length,
##    self.bit_offset)
    
if __name__ == "__main__":
    print("Running Unit Test\n")
    def construct_UDP_header():
    
        with Internet_Wire_Format() as UDP:
            UDP.boundary(32) # Set boundary.
                             # IETF headers are usually assumed to begin on
                             # a bit address that is a multiple of 2**32
            
            UDP.field("Source Port",0,Nat,16) # (0-15)
            UDP.field("Destination Port",1,Nat,16) # (16-31)
            UDP.field("Length",2,Nat,16) # (32-47) and
            UDP.field("Checksum",3,Nat,16) # (48-63)
            #UDP.field("data_octets",4,Nat,64)

            UDP.boundary(32)  # this could be the basis for an attack exercise 
        return UDP
    UDP = construct_UDP_header()
    #UDP.data_octets.data_value = 123456
    UDP.Source_Port.data_value=0x11
    UDP.Destination_Port.data_value=5280 # Layer4.TransientPort()
    UDP.Length.data_value = 32
    print(UDP)
##    UDP.NextProtocolValue = 33
##    print(UDP_Header.NextProtocol)
##    
 
