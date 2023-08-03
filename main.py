from server import Server

HOST = '192.168.0.146'
PORT = 9090
INFO = 'version: 0.2.1; creation date : 03.08.2023r'

server = Server(HOST, PORT, INFO)

server.start()