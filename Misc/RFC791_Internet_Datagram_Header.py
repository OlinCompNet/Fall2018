# RFC791  Internet Datagram Header

IPv4_Wire_Format="""
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    ==>         original field names left just for comparison     <==
    |Version|  IHL  |Type of Service|          Total Length         |
    |{0:^7s}|{2:^7s}|{4:^15s}|{6:^31s}| 
    |{1:^7d}|{3:^7d}|{5:^15d}|{7:^31d}| 
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |         Identification        |Flags|      Fragment Offset    |
    |                               |     |                         |
    |                               |     |                         |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |  Time to Live |    Protocol   |         Header Checksum       |
    |               |               |                               |
    |               |               |                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                       Source Address                          |
    |                                                               |
    |                                                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Destination Address                        |
    |                                                               |
    |                                                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 20 |                    Options                    |    Padding    |
    |                                               |               |
    |                                               |               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

                        IPv4 Wire Format
"""
if __name__ == "__main__":
    print(1)
    # the datafields are now self-centering!
    
    fields=("Version",4,"IHL",5,"Type_of_Service",10,"Total_Length",50)
    #         0       1   2   3   4                5       6            7
    # note alternating name and value - see impementation note below
    print(2)
    print(IPv4_Wire_Format.format(*fields))

    # Impementation note: we will change from hand-coded fields
    #("Version",4,"IHL",5, ...) to automatically generated ones
    # by using an ordered dictionary algorithm for the final
    # product
    print(3)
    

    # the main issue now is finishing the little compiler we need
    # to change class variable names 
    # (class variables are bound at compile time)
    #
