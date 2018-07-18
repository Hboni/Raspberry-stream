import socket
import os


class Server:
    """
    Create a server that prints what it received

    You can link a server to a certain port on localhost.
    Each time the server receives data, it decode it into a string and print it.

    To stop the server, use a Client to send a message "fin"
    """

    def __init__(self, address, host="localhost", timeout=2):

        # AF_INET is the type of protocol used (AF_UNIX/AF_INET/AF_INET6)
        # SOCK_STREAM is the socket type
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.bind((host, address))
        self.socket.settimeout(timeout)
        print('socket connected to the address {}'.format(address))

    def begin_listen(self):

        self.socket.listen(5)
        client, address = "", ""
        while not client:
            try:
                client, address = self.socket.accept()
            except socket.timeout:
                pass

        print("{} connected".format(address))

        response = ""
        while not response == "fin":
            try:
                response = client.recv(1024).decode()
            except socket.timeout:
                pass

            if response[:4] == "open":
                site = response.split(' ')[1]
                command = "xdg-open "
                command += site
                os.system(command)
            elif response:
                print(response)

        client.send("Bye".encode())
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
