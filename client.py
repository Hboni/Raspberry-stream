import socket


class Client:
    """
    Create a client socket that link to a certain port, and communicate with the server.

    The aim of this Client is to connect to a server through a port.
    After correctly connected, you can send messages/data to the server using the
    chat_with_server function, that can send several messages.

    To stop the client, send the message "fin"

    """

    def __init__(self, port, host="localhost"):
        self.host = host
        self.port = int(port)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        #self.socket.setblocking(0)
        self.socket.settimeout(2)
        print("Connection on {}".format(self.port))

    def send_message(self, message):
        self.socket.send(message.encode())

        response = ""
        while not response:
            response = self.socket.recv(1024)
            print(response.decode())

        print("Close")
        self.socket.close()


    def chat_with_server(self):
        mess = input("Which message to send to the server : \n")

        server_response = ""
        while mess != "fin":
            self.socket.send(mess.encode())
            try:
                server_response = self.socket.recv(1024)
            except socket.timeout:
                pass
            print(server_response)
            mess = input(">>> ")

        self.socket.send(mess.encode())

        server_response = self.socket.recv(1024)
        print(server_response.decode())
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
