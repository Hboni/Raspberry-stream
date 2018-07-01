import socket


class Client:

    def __init__(self, address):
        self.hote = "localhost"
        self.port = address

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.hote, self.port))
        print("Connection on {}".format(self.port))

    def send_message(self):
        self.socket.send("Hey my name is Hugo!".encode())

        response = ""
        while not response:
            response = self.socket.recv(1024)
            print(response.decode())

        print("Close")
        self.socket.close()


if __name__ == '__main__':
    hote = "localhost"
    port = 15555
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((hote, port))
    print("Connection on {}".format(port))

    response = ""
    while not response:
        socket.send('Hello world'.encode())
        response = socket.recv(1024)
        print("<"+response.decode())

    print("Close connexion")
    socket.close()
