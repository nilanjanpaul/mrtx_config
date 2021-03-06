#!/usr/bin/env python

#Usage: ./rc.py "cmd"
# >     ./rc.py "set rxfreq 2450e6"
# >     ./rc.py "get rxfreq"
#

# Example commands:
# python rc.py node1-1 5111 "rxfreq all"
# python rc.py node1-1 5111 "rxfreq all 2400e6"

# python rc.py node1-1 5111 "rxgain all"
# python rc.py node1-1 5111 "rxgain all 11"

# python rc.py node1-1 5111 "rxrate all"

# python rc.py node1-1 5111 "txfreq all"
# python rc.py node1-1 5111 "txfreq all 3400e6"

# python rc.py node1-1 5111 "txgain all"
# python rc.py node1-1 5111 "txgain all 12"

# python rc.py node1-1 5111 "txrate all"

# python rc.py node1-1 5111 "rxhold on"
# python rc.py node1-1 5111 "rxhold off"

import sys
import socket
import struct
from time import time

TCP_IP = sys.argv[1]
TCP_PORT = int(sys.argv[2])
#TCP_IP = sys.argv[1]  #"node1-1.sb3.orbit-lab.org"
#TCP_PORT = int(5180)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

COMMAND =  sys.argv[3]
s.sendall(COMMAND)
data = s.recv(256*50)

print data

s.close()
