
def raise_AttributeError(msg):
    raise AttributeError(msg)

def OTrace(X):
    print("\n\tOTrace:\n\t"+X)
    return True
 
class DescriptorBase    :
    """
A data descriptor that sets and returns values normally.
It "OTraces" accesses to a value because it is often difficult
to see if a Descriptor is working
"OTracing" can be removed by compiling DescriptorBase with the -O option.
"""
    def __init__(
        self,
        name=None,
        value=None
        ):
        print(
            "DescriptorBase(name={!r:},value={!r:},value_type={!r:})".format(
                name,value,type(value)))
        self.name = name
        self.value = value
        assert OTrace("""
__init__(self,
         name='{0:}',
         value={1:},
         )
         """.format(self.name,self.value))
           
    def __get__(self,obj,objtype):
        
        assert OTrace("{0:}.__get__() -> {1:}".format(self.name,self.value))
        
        return self.value
    
    def __set__(self,obj,value):
        
        assert OTrace("{0:}.__set__({1:}) # from {2:}".format(
            self.name,value,self.value))

        self.value = value
        return


if __name__ == "__main__":
    class TestClass:
        x = DescriptorBase("x",10)
        y = 5

    m = TestClass()
    print ("m.x")
    print(m.x)
    print("m.x = 20")
    m.x = 20
    print("m.x")
    print(m.x)
    
    
    


        

