#
## Internet Checksum
## See RFC1071
#

def Calc_16_bit_checksum(I:int)->int:
    while I>>16:
        I = (I&0xffff)+(I>>16)
    return I

def Calc_byte_checksum(X:bytes)->bytes:
    
    if len(X)%2:
        X += bytes([0]) # make len(X) even
    
    I = int.from_bytes(X,"big") # convert X to int
    CS = Calc_16_bit_checksum(I) # produce int checksum

    return CS.to_bytes(2,"big",signed=False) #








if __name__ == "__main__":
    print("HELLO")
    print("assert 0")  
    assert Calc_byte_checksum(bytes([0,1,255,254])) == bytes([0xff,0xff])kkkkkkkkkkkkkkk

# Notes and standard checksum tests from RFC1071
#
# 1 wire format convention for separating
#   checksum value from calculation of checksum
# 2 vulnerability of checksum for attack (q.v.)
# 3 RFC 1071 Computing the Internet Checksum  September 1988
#
## Numerical Examples
##
##       We now present explicit examples of calculating a simple 1's
##       complement sum on a 2's complement machine.  The examples show the
##       same sum calculated byte by bye, by 16-bits words in normal and
##       swapped order, and 32 bits at a time in 3 different orders.  All
##       numbers are in hex.
    print("assert 1")
    assert Calc_byte_checksum(
        bytes([0x00,0x01,0xf2,0x03,0xf4,0xf5,0xf6,0xf7])
        ) == bytes([0xdd,0xf2])

##                      Byte-by-byte    "Normal"  Swapped
##                                        Order    Order
##
##            Byte 0/1:    00   01        0001      0100
##            Byte 2/3:    f2   03        f203      03f2
##            Byte 4/5:    f4   f5        f4f5      f5f4
##            Byte 6/7:    f6   f7        f6f7      f7f6
##                        ---  ---       -----     -----
##            Sum1:       2dc  1f0       2ddf0     1f2dc
##
##                         dc   f0        ddf0      f2dc
##            Carrys:       1    2           2         1
##                         --   --        ----      ----
##            Sum2:        dd   f2        ddf2      f2dd
##
##            Final Swap:  dd   f2        ddf2      ddf2
##
##
##            Byte 0/1/2/3:  0001f203     010003f2       03f20100
##            Byte 4/5/6/7:  f4f5f6f7     f5f4f7f6       f7f6f5f4
##                           --------     --------       --------
##            Sum1:         0f4f7e8fa    0f6f4fbe8      0fbe8f6f4
##
##            Carries:              0            0              0
##
##            Top half:          f4f7         f6f4           fbe8
##            Bottom half:       e8fa         fbe8           f6f4
##                              -----        -----          -----
##            Sum2:             1ddf1        1f2dc          1f2dc
##
##                               ddf1         f2dc           f2dc
##            Carrys:               1            1              1
##                               ----         ----           ----
##            Sum3:              ddf2         f2dd           f2dd
##
##            Final Swap:        ddf2         ddf2           ddf2
##
##
##
##
##
##    Braden, Borman, & Partridge                                     [Page 5]
##
##     
##    RFC 1071            Computing the Internet Checksum       September 1988
##
##
##       Finally, here an example of breaking the sum into two groups, with
##       the second group starting on a odd boundary:
##
    print("assert 2")
    assert Calc_byte_checksum(bytes([0,1,0xf2]))==bytes([0xf2,0x01])
    print("assert 3")
    assert Calc_byte_checksum(bytes([0x03,0xf4,0xf5,0xf6,0xf7])) == bytes([0xf0,0xeb])

##
##                       Byte-by-byte    Normal
##                                        Order
##
##            Byte 0/1:    00   01        0001
##            Byte 2/ :    f2  (00)       f200
##                        ---  ---       -----
##            Sum1:        f2   01        f201
##
##            Byte 4/5:    03   f4        03f4
##            Byte 6/7:    f5   f6        f5f6
##            Byte 8/:     f7  (00)       f700
##                        ---  ---       -----
##            Sum2:                      1f0ea
##
##            Sum2:                       f0ea
##            Carry:                         1
##                                       -----
##            Sum3:                       f0eb
##
##            Sum1:                       f201
##            Sum3 byte swapped:          ebf0
##                                       -----
##            Sum4:                      1ddf1
##
##            Sum4:                       ddf1
##            Carry:                         1
##                                       -----
##            Sum5:                       ddf2
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##    Braden, Borman, & Partridge                                     [Page 6]
##
##     
##    RFC 1071            Computing the Internet Checksum       September 1988
##
    print("rfc1071 tests passed")
