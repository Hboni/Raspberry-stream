import socket


class Client:

    def __init__(self, address):
        self.hote = "localhost"
        self.port = address

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.hote, self.port))
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
