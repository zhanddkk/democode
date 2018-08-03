import socket
import socks
import threading
import time


class Client(threading.Thread):
    def __init__(self, remote, remote_port):
        super(Client, self).__init__()
        # self.__udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__udp_socket = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__udp_socket.set_proxy(socks.PROXY_TYPE_SOCKS5, addr='10.218.117.35', port=1080)
        self.__server = (remote, remote_port)
        # self.__udp_socket.connect((remote, remote_port))
        pass

    def send(self, data):
        # self.__udp_socket.send(data)
        self.__udp_socket.sendto(data, self.__server)
        pass

    def run(self):
        _i = 0
        while True:
            data = self.__udp_socket.recv(1024)
            if len(data) > 0:
                print('{}: {}'.format(_i, data))
                _i += 1
        pass
    pass


if __name__ == '__main__':
    c = Client('www.movif.club', 23)
    # c.start()
    while True:
        c.send(b'abcedef')
        time.sleep(2)
        pass
    pass
