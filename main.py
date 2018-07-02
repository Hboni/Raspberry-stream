from server import Server
from client import Client

port = 15555
choice = input("Server [s] or Client [c] ? ")

if choice == 's':
    serv = Server(port)
    serv.begin_listen()

elif choice == 'c':
    client = Client(port)
    mess = input("Which message to send to the server ? :\n")
    # client.send_message(mess)
    client.chat_with_server()
