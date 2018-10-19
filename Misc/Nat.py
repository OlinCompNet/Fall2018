# Nat with bitwidth
import functools
def value_check(bit_length,value):
    return value

##        if type(value) is not int:
##            raise AttributeError("Not int")
##        elif value < 0:
##            raise AttributeError("Value less than 0")
##        elif value.bit_length() > bit_length:
##             raise AttributeError(
##                 "Value not less than 2**{}".format(bit_length)) 
##        else:
##            return value

import DescriptorBase
        
class Nat(DescriptorBase.DescriptorBase):
    print(DescriptorBase)
    
    def __init__(self,
                 name = None,
                 value= None,
                 bit_length = None):
        "Nat(name:str,value,bit_length)"
        print("in Nat")
        print("""__init__(name={},
                          value={},
                          bit_length={}
                          )""".format(name,value,bit_length))
        self.name=name
        self.value=value

        if not type(name) is str:
            raise AttributeError("name must be a str")
        if not bit_length:
            raise AttributeError("bit_length must be specified")
        elif not type(bit_length) is int or bit_length < 1:
            raise AttributeError("bit_length must be a positive int")
        else:
            pass
        #super().__init__(
          #  name=name,
           # value=value)
            #value_check = lambda X:X)
            #raiseAttributeError("X>3") if X>3 else X)
            #functools.partial(value_check,bit_length))
        print("super returned")
        return
       
    
    

if __name__ == "__main__":
    
    print("t1.n1")  
    class T1:
        n1 = Nat(name="n1",
                    value = 0,
                    bit_length = 2)
        
        
    print(T1.n1)
    T1.n1 = 1
    print(T1.n1)
    T1.n1 = 2
    print(T1.n1)
    T1.n1 = -1
    print(T1.n1)
    
