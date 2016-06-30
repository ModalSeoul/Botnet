from socket import *
import sys

sock = socket(AF_INET, SOCK_STREAM)
SERVER_ADDRESS = (sys.argv[2], 25000)
sock.connect(SERVER_ADDRESS)

try:
    message = sys.argv[1]
    sock.sendall(message)
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
finally:
    print('done')
