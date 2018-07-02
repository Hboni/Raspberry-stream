from server import Server
from client import Client

port = 15555
choice = input("Server [s] or Client [c] ? ")

if choice == 's':
    serv = Server(port)
    serv.begin_listen()

elif choice == 'c':
    client = Client(port)
    # client.send_message(mess)
    client.chat_with_server()
