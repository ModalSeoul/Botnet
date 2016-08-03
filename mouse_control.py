import sys
from socket import *
from time import sleep
from pymouse import PyMouse

sock = socket(AF_INET, SOCK_STREAM)
SERVER_ADDRESS = (sys.argv[1], 25000)
sock.connect(SERVER_ADDRESS)

m = PyMouse()
while 1:
    sock.sendall(str(m.position()))
    sleep(0.1)
