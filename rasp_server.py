import os
import argparse
import socket
from server import Server

### Mandatory parameters
parser = argparse.ArgumentParser(description="Launch a raspberry stream server.")

parser.add_argument('--address', '-ad', required=True,
                    help='Address of the server')
parser.add_argument('--port', '-p', required=True,
                    help='Port to listen')

### Optionnal parameters
parser.add_argument('--timeout', '-t', required=False,
                    help='Timeout of the server')

## Get parameters in variables
args = vars(parser.parse_args())
address = args.pop('address')
port = args.pop('port')
timeout = args.pop('timeout')

### Init of socket
server = Server(address, port, timeout)
server.begin_listen()
# socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# try:
#     socket.bind((address, port))
#     print('Server bind to {}:{}'.format(address, port))
# except:
#     print('Server not able to bind to {}:{}'.format(address, port))
#
# if timeout:
#     socket.settimeout(timeout)
# else:
#     socket.settimeout(2)