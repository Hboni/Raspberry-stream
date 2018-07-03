from server import Server
from client import Client

choice = input("Server [s] or Client [c] ? ")
port = input("Which port to use ? ")
if not port:
    port = 14142

if choice == 's':
    serv = Server(port)
    serv.begin_listen()

elif choice == 'c':
    client = Client(port)
    # client.send_message(mess)
    client.chat_with_server()
