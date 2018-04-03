import socketserver
import socket
import threading
import time


class UdpMessageHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        data = self.request[0]
        print('Received form {}:'.format(self.client_address),
              '{}'.format(', '.join('{:02X}'.format(byte) for byte in data)))
        self.socket.sendto(data, self.client_address)
        # print(self.server)
    pass


class Server:
    def __init__(self, local, local_port):
        self.__udp_server = socketserver.ThreadingUDPServer((local, local_port), UdpMessageHandler)
        self.__udp_socket = self.__udp_server.socket
        self.__udp_server_thread = None
        pass

    def start(self):
        self.__udp_server_thread = threading.Thread(target=self.__udp_server.serve_forever)
        self.__udp_server_thread.daemon = True
        self.__udp_server_thread.start()
        pass

    def stop(self):
        self.__udp_server.shutdown()
        self.__udp_server.server_close()
        pass

    def send(self, data):
        self.__udp_socket.send(data)
        pass
    pass


def main():
    s = Server('', 8000)
    s.start()
    while True:
        time.sleep(1)
        pass
    pass


def compress():
    import zlib
    from urllib import request
    print(time.time())
    fp = request.urlopen('http://www.baidu.com')
    str = fp.read()
    fp.close()

    # ---- 压缩数据流。
    print(time.time())
    str1 = zlib.compress(str, zlib.Z_BEST_COMPRESSION)
    print(time.time())
    str2 = zlib.decompress(str1)
    print(time.time())
    print(len(str))
    print(len(str1))
    print(len(str2))
    print(str1)
    print(str2)
    pass


if __name__ == '__main__':
    compress()
    pass
