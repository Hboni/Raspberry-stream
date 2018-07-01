import socket


class Server:

    def __init__(self, address):

        # AF_INET is the type of protocol used (AF_UNIX/AF_INET/AF_INET6)
        # SOCK_STREAM is the socket type
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.bind(('localhost', address))
        print('socket connected to the address {}'.format(address))

    def begin_listen(self):

        self.socket.listen(5)
        client, address = self.socket.accept()
        print("{} connected".format(address))

        response = ""
        while not response:
            response = client.recv(1024)
            if response:
                print(response.decode())
                client.send("Hey".encode())

        print("Close")
        client.close()
        self.socket.close()


if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.bind(('', 15555))
    print('socket connected to the address {}'.format(15555))

    socket.listen(5)
    client, address = socket.accept()
    print("{} connected".format(address))

    response = ""
    while not response:

        response = client.recv(1024)
        print(">"+response.decode())
        if response:
            client.send(b"Hey")

    print("Close")
    client.close()
    socket.close()