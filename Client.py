import socket

class Client:
    HOST = '192.168.0.146'
    PORT = 9090

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))

    def send_recive(self):
        while True:
            user_input = input('Enter your message: \nType help for command list:\n').encode('utf-8')
            self.client_socket.sendall(user_input)
            data = self.client_socket.recv(1024).decode('utf-8')
            if data == 'server closed':
                print(data)
                break
            else:
                print(data)

if __name__ == '__main__':
    client = Client()
    client.send_recive()