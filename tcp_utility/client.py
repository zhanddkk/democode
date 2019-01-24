import socket


if __name__ == '__main__':
    _tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _tcp.connect(('10.218.117.35', 1080))
    _tcp.send(b'\x05\x01\x00')
    _data = _tcp.recv(1024)
    print(_data)

    _udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _udp.sendto(b'\x05\x01\x00', ('10.218.117.35', 1080))
    _data = _tcp.recv(1024)
    print(_data)
    pass
