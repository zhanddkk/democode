import socket
import threading
import time


class Client(threading.Thread):
    def __init__(self, remote, remote_port):
        super(Client, self).__init__()
        self.__udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__udp_socket.connect((remote, remote_port))
        pass

    def send(self, data):
        # self.__udp_socket.send(data)
        self.__udp_socket.sendto(data, ('192.168.1.102', 8000))
        pass

    def run(self):
        while True:
            data = self.__udp_socket.recv(1024)
            print(data)
        pass
    pass


if __name__ == '__main__':
    c = Client('47.254.42.105', 8000)
    while True:
        c.send(b'abcedef')
        time.sleep(2)
        pass
    pass
