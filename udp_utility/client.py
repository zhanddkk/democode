import socket
import threading
import time


class Client(threading.Thread):
    def __init__(self, remote, remote_port):
        super(Client, self).__init__()
        self.__udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__server = (remote, remote_port)
        # self.__udp_socket.bind(('192.168.1.102', 8001))
        pass

    def send(self, data):
        self.__udp_socket.sendto(data, self.__server)
        # self.__udp_socket.send(b'12345')
        pass

    def run(self):
        _i = 0
        print('client started')
        while True:
            data = self.__udp_socket.recv(1024)
            if len(data) > 0:
                print('{}: {}'.format(_i, data))
                _i += 1
                pass
            pass
        pass
    pass


if __name__ == '__main__':
    # 10.218.117.35
    c = Client('192.168.1.102', 1081)
    c.start()
    while True:
        c.send(b'\x05\x01\x00')
        time.sleep(2)
        pass
    pass
