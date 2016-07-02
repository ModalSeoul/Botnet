from socket import *
import os
import sys

sock = socket(AF_INET, SOCK_STREAM)
SERVER_ADDRESS = (sys.argv[2], 25000)
sock.connect(SERVER_ADDRESS)


def ls_dir(dir):
    dir_list = []
    ls_path = os.popen('ls {}'.format(dir)).read()
    split_items = ls_path.split('\r')
    for item in split_items:
        item = item.split('\n')[0]

try:
    message = sys.argv[1]
    sock.sendall(message)
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        _ls = 'ls '
        if _ls in str(data):
            _dir = str(data).split()[1]
            sock.sendall(ls_dir(_dir))

finally:
    print('done')
