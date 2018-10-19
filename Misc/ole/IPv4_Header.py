# RFC791  Internet Datagram Header

IPv4_Header_Format="""
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

                   Example Internet Datagram Header

                               Figure 4.
"""
if __name__ == "__main__":
    # the datafields are now self-centering!
    
    fields=("Version",4,"IHL",5,"Type_of_Service",10,"Total_Length",50)
    #         0       1   2   3   4        5       6            7   
    print(IPv4_Header_Format.format(*fields))

    # Note: we will change from hand-coded fields
    #("Version",4,"IHL",5, ...) to automatically generated
    # from ordered dictionary type --> later
    # No time just now.

    # the main issue now is finishing the little compiler we need
    # to change class variable names 
    # (class variables are bound at compile time)
    #
