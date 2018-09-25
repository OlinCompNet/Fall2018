#
## sample_subprocess to be used for pid to subprocess mapping in server
#

import sys # get access to arguments supplied to python subprocess

#
## subprocess should use logging to send status and problem outputs
## since this will allow consolidation of events in two sides of
## session.
##
## Use logging to send output to log file for subprocess
#
## The following follows the first example in the "Logging HOWTO" section
## of the python 3.3 documentation 
#
import time
import logging
logging.basicConfig(filename='loggingexample.log',level=logging.DEBUG)
logging.debug("\nStarting sample_subprocess at time {}".format(time.asctime()))
argv = sys.argv
logging.debug('\n\n sys.argv was {}\n\n'.format(argv))
logging.debug("len(sys.argv) was {}\n".format(len(argv)))
ipaddress = argv[1]
portaddress = int(argv[2])
logging.debug("next step is to open a socket in this subprocess")
logging.debug("then call sock.send_to(({},{}),message)".format(repr(ipaddress),portaddress))
logging.debug("\nEnding sample_subprocess at time {}".format(time.asctime()))
