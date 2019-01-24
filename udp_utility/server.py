import socket
# import threading


class UdpServer:
    def __init__(self, local, port):
        self.__socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.__socket.bind(('::', 8081))
        while True:
            _data, _address = self.__socket.recvfrom(1024)
            # self.__socket.sendto(b'OK', _address)
            print('[{}]: {}'.format(_address, _data))
            pass
        pass
    pass


def main():
    a = UdpServer('::', 8080)

    pass


if __name__ == '__main__':
    main()
    pass
