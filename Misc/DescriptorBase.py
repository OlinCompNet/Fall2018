def raise_AttributeError(msg):
    raise AttributeError(msg)

def OTrace(X):
    print("\n\tOTrace:\n\t"+X+"\n\tOTrace end.")
    
    return True

class DescriptorBase(object):
    """
A data descriptor that sets and returns values normally.
It "OTraces" accesses to a value because it is often difficult
to see if a Descriptor is working
"OTracing" can be removed by compiling DescriptorBase with the -O option.
"""
    def __init__(
        self,
        name=None,
        value=None,
        value_check=lambda X:X if X>2 else raise_AttributeError("{:} <= 2".format(X))
        ):
        self.name = name
        self.value = value
        self.value_check = value_check

        assert OTrace("""
\t\t__init__(self='{0:}',
\t\tname='{1:}',
\t\tvalue={2:},
\t\tvalue_check={3:}
         )
         """.format(self.__class__.__name__,self.name,self.value,self.value_check))
           
    def __get__(self,obj,objtype):
        
        assert OTrace("{0:}.__get__() -> {1:}".format(self.name,self.value))
        
        return self.value
    
    def __set__(self,obj,value):
        
        assert OTrace("{0:}.__set__({1:}) # from {2:}".format(
            self.name,value,self.value))

        self.value = (self.value_check(value),)[0]
        return


if __name__ == "__main__":
    class TestClass:
        x = DescriptorBase("x",10)
        y = 5
    print("instatiate TestClass")
    m = TestClass() # instance of TestClass that contains DescriptorBase 
    print ("m.x")
    print(m.x)
    print("m.x = 20")
    m.x = 20
    print("m.x")
    print(m.x)
    print("Attempt to set m.x to -1 when -1 is outside of domain")
    print("m.x = -1")
    m.x = -1
    
    
    


        

