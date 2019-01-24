import socket
# import socks
import threading
import time


class Client(threading.Thread):
    def __init__(self, remote, remote_port):
        super(Client, self).__init__()
        self.__udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__server = (remote, remote_port)
        pass

    def send(self, data):
        self.__udp_socket.sendto(data, self.__server)
        pass

    def run(self):
        _count = 0
        print('client started')
        while True:
            data = self.__udp_socket.recvfrom(1024)
            if len(data) > 0:
                print('{}: {}'.format(_count, data))
                _count += 1
        pass
    pass


if __name__ == '__main__':
    c = Client('10.177.58.51', 8081)
    c.start()
    while True:
        c.send(b'abcedef')
        time.sleep(2)
        pass
    pass
