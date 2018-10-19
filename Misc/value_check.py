
def value_check(value):
    if issubclass(type(value),Nat):
        return value.value_check(value)
    if issubclass(type(value),Chr):
        return value.value_check(byte_length,value)
    return value

