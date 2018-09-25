#
##  Network Calculator (Integers only)
#

class calc:
    "instruction set"
    def __init__(self):
        self.clear("")
        
    def add(self,operand):
        self.acc += int(operand)
        return format( self.acc)
    
    def mul(self,operand):
        self.acc *= int(operand)
        return format(self.acc)
    
    def sub(self,operand):
        self.acc -= int(operand)
        return format(self.acc)
    
    def div(self,operand):
        divisor = int(operand)
        if divisor:
            self.acc //= divisor
            return format(self.acc)
        else:
            return "ZERO DIVIDE"
        
    def clear(self,operand):
        self.acc = 0
        return format(self.acc)
    
    def display(self,operand):
        return format(self.acc)

    def help(self,value):
        return  """ENTER REQUEST LETTER THEN INTEGER VALUE
REQUEST        COMMAND       

HELP           H
END SESSION    E
CLEAR          C
ADD 134        A 134
SUBTRACT 78    S 78
MULTIPLY 33    M 33
DIVIDE 11      D 11
"""
    


if __name__ == "__main__":
    calcx = calc()
    print(
"""
WELCOME TO CALCULATOR
ENTER H FOR HELP
""")
    while 1:
        calc_req = input("COMMAND ").strip().upper()
      
        if not calc_req:
            continue

        calc_opcode = calc_req[0]
        
        if not calc_opcode in "DECASMH":
            print("ENTER E TO EXIT OR H FOR HELP")
            continue

        calc_operand = calc_req[1:].strip()
        
        print(format({
            "E":calcx.display,
            "C":calcx.clear,
            "A":calcx.add,
            "S":calcx.sub,
            "M":calcx.mul,
            "D":calcx.div,
            "H":calcx.help}[calc_opcode](calc_operand)
          ))
        if calc_opcode == "E":
            print("FAREWELL")
            break

    
