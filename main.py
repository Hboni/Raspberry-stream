from server import Server
from client import Client

choice = input("Server [s] or Client [c] ? ")
host = input("Which server address ? ")
port = int(input("Which port to use ? "))

if not port:
    port = 14142

if choice == 's':
    serv = Server(port, host)
    serv.begin_listen()

elif choice == 'c':
    if host:
        client = Client(port, host)
        client.connect()
    else:
        client = Client(port)
    # client.send_message(mess)
    client.test_connection()
    # client.chat_with_server()
