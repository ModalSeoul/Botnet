import os
import sys
from socket import *
from time import sleep
from pymouse import PyMouse

sock = socket(AF_INET, SOCK_STREAM)
SERVER_ADDRESS = (sys.argv[2], 25000)
sock.connect(SERVER_ADDRESS)


def listen_mouse():
    m = PyMouse()
    while 1:
        data = sock.recv(16)
        _pos = data
        _x = _pos.split('(')[1].split(',')[0]
        _y = _pos.split(' ')[1].split(')')[0]
        m.move(int(_x), int(_y))
        sleep(0.1)

try:
    message = sys.argv[1]
    sock.sendall(message)
    amount_received = 0
    amount_expected = len(message)
    listen_mouse()

    while True:
        data = sock.recv(16)
        cmd = os.popen(data).read()
        sock.send(str.encode(cmd))

finally:
    print('done')
