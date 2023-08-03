import socket
import json
from datetime import datetime

class Server:

    def __init__(self, host, port, info):
        self.host = host
        self.port = port
        self.info = info
        self.start_time = datetime.now()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

    def server_commands(self):
        msg={
            'uptime': "return lifetime server",
            'info': 'return version of server',
            'help': 'return help for server commands',
            'stop': 'stop server and client',
        }
        return json.dumps(msg,indent=1)

    def uptime(self):
        return json.dumps(str(datetime.now() - self.start_time),indent=1)

    def json_unpack(self,data):
        unpack_data = []
        unpack_data = data.split(' ')
        return unpack_data

    def start(self):

        connection, client_address = self.server_socket.accept()

        print(f'Connection from {client_address}')
        while True:
            query = connection.recv(1024).decode('utf-8')

            if not query:
                break

            query_list = self.json_unpack(query)

            if query_list[0] == 'uptime':
                connection.send(self.uptime().encode('utf-8'))
            elif query_list[0] == 'info':
                connection.send(self.info.encode('utf-8'))
            elif query_list[0] == 'help':
                connection.send(self.server_commands().encode('utf-8'))
            elif query_list[0] == 'stop':
                connection.send(('server closed').encode('utf-8'))
                self.server_socket.close()
                break
            else:
                connection.sendall((f'Bad command').encode('utf-8'))