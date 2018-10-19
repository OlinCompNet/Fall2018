# # The IPv4 header has 32 bit (4 byte) integer values
                          # (Source Address and Destination Address)
                          # On most computer archiectures with byte
                          # addressing 32 bit integer registers can
                          # only be loaded from addresses that are
                          # multiples of 32 bits (multiples of 4 bytes)
                          # Therefore IPv4 headers in memory 
                          # must start on a 32 bit (4 byte) address
                          # This is also true for 64 bit and 128 bit values                        # note that the length of the IPv4 header
                                  # in bits is IHL*32. The minimum value of 

# IHL                             is 5 (160 bits or 20 bytes)
                                  # IHL is a 4 bit value so
                                  # the largest IHL value is 15, so the 
                                  # longest possible Internet header length
                                  # is 480 bits or 60 bytes
               

                   # Note further that in order to determine
                                  # the actual header length, one must first
                                  # decode the header as if IHL were 5
                                  # then decode the remaining 0 to 40 bytes
                                  # 
