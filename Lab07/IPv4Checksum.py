#
## One's complement arithmetic and IPv4 checksum
## see Wikipedia: http://en.wikipedia.org/wiki/IPv4_header_checksum
#
#
def p(X):
    print(X)
    return X

def halfword(X):
    " two ints (from bytes, bytearray, list, tuple ...) between 0 and 255 to a 16-bit word (halfword)"
    if not (len(X)==2) and all(0<x<256 for x in X):
            raise ValueError("X be two ints between 0 and 255")
    return int(X[0])*256 + int(X[1])

def halfwords(X):
    " convert even-length string of bytes to halfwords "
    if len(X)%2:
        raise ValueError("len(X) must be multiple of 2")
    return [halfword(X[i:i+2]) for i in range(0,len(X),2)]

def flip(X):
    " reverse the order of the elements of an interator"
    return X[-1::-1]
    
def hex2int(X):
    "convert a hex number of any length to an int"
    return sum([("0123456789ABCDEF".index(v))*16**k for k,v in enumerate(flip(X.upper()))])
    

def IPv4_checksum(X):
    "Calculate the IPv6 checksum for a list of halfwords"
    sumX = sum(X)
    while sumX > 2**16:
        sumX = (sumX%2**16) + sumX//2**16 # add carries (i.e. non-zero values for sumX//2**16)
    return (~sumX)%2**16  

if __name__ == "__main__":
    ## Wikipedia Test Case:http://en.wikipedia.org/wiki/IPv4_header_checksum
    Wikitest_minus_checksum = [hex2int(hx) for hx in "4500 0073 0000 4000 4011 c0a8 0001 c0a8 00c7".split(" ")]
    chk = IPv4_checksum(Wikitest_minus_checksum)
    print(hex(chk))
    Wikitest = [hex2int(hx) for hx in "4500 0073 0000 4000 4011 b861 c0a8 0001 c0a8 00c7".split(" ")]
    chk = IPv4_checksum(Wikitest)
    print(hex(chk))


## One's complement
##
## In the following table from the wikipedia page wikipedia.org/fr/Complement_a_un, you can see that the 
## negative of a binary value in one's complement arithmetic is obtained by simply inverting each binary value.  
## becomes 1 and 1 becomes 0.  Some early computers such at the DEC PDP/1 used this number representation.
##
##"
## Example: tHere are all sixteen one's complement representations between -7 and 7.
## Note that this number representation has two zeros, which are normally considered equivalent
##
## Décimal    +      −
##    0      0000   1111   +0 and -0 are True if tested for 0, False otherwise.
##    1      0001   1110
##    2      0010   1101
##    3      0011   1100
##    4      0100   1011
##    5      0101   1010
##    6      0110   1001
##    7      0111   1000
##
##To represent this in Python, we create a class group consisting of a set with fifteen elements.
## 1 to 7, -1 to -7, and 1111 for zero.
##  Addition (a+b) is performed modulo 16.  
##  Negation (-b)  is performed by inverting the value of each bit in the representation




