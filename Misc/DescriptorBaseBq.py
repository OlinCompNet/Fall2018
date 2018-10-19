
OTRACING = 0

def raise_AttributeError(msg):
    raise AttributeError(msg)

def OTrace(X):
    if OTRACING:
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
        value=None,
        **D
        ):
        assert OTrace(
            """
DescriptorBase.__init__(self,
        name={!r:},
        value={!r:},
        D={!r:})
        """.format(name,value,D))
        for k,v in D.items():
            setattr(self,k,v)
        self.name = name
        self.value = self.value_check(value)

##    def __enter__(self):
##        self.value = self.hold
##        return self
##
##    def __exit__(self,a,b,c):
##        #del self.value
##        return a==b==c==None
    def value_check(self,value):
        return True
        
    def __get__(self,obj,objtype):
        
        assert OTrace("{0:}.__get__() -> {1:}".format(self.name,self.value))
        
        return self.value
    
    def __set__(self,obj,value):
        assert OTrace("__set__({},{}".format(obj,value))
        if not(self.value_check(value)):
            raise AssertionError("valuecheck failed")

        assert OTrace("self.valuecheck({}) -> Pass".format(value))

        assert OTrace("{0:}.__set__({1:}) # from {2:}".format(
            self.name,value,self.value))

        self.value = value

        return
 

if __name__ == "__main__":
    class Nat(DescriptorBase):       
        def value_check(self,value):
            assert OTrace("value_check mro: {}.".format(self.__class__.mro()))
            if type(value) is not int:
                raise AttributeError("value type not int\n")
            if value < 0 :
                raise AttributeError("value < 0\n")
            if value.bit_length() > self.max_bit_length:
                raise AttributeError(
                    """
value.bit_length() > self.max_bit_length")
            {:>d}  > {:<d}
            
                    """.format(value.bit_length(),self.max_bit_length))
            return True

            
    class TestClass:
        x = Nat("x",2,max_bit_length=3)
        y = 5

        

    m = TestClass()
    print ("m.x")
    print(m.x)
    print("m.x = 5")
    m.x = 5
    print("m.x")
    print(m.x)
    try:
        print("m.x = 'abc'")
        m.x = "abc"
    except AttributeError as e:
        print(e)
    try:
        print("m.x = -3")
        m.x = -3
        print("m.x")
        print(m.x)
    except AttributeError as e:
        print(e)
        
    try:
        print("m.x=30")
        m.x=30
        print("m.x")
        print(m.x)
    except AttributeError as e:
        print(e)
        
    
    


        

