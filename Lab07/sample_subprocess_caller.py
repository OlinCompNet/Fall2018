#
## sample_subprocess_caller
## uses subprocess.call to launch
## roundsubprocess
##
## passes arguments (ip_address,port_address)
## note that arguments are passed as str values
#
import os
if os.path.exists("loggingexample.log"):
    os.remove("loggingexample.log")
import subprocess
# call subprocess
print("launching subprocess 'sample_subprocess.py'")
return_code = subprocess.call(["python","sample_subprocess.py","192.168.0.1","45321"])
print("subprocess.call(...) returned code {}".format(return_code))
print("Following is information from file 'loggingexample.log'")
print("Note that this file contains old information which would normally be filtered out by log reader")
print((open("loggingexample.log").read()))
