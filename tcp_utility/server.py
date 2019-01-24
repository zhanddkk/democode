import socketserver


class TcpServerHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        _data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(_data)
        # just send back the same data, but upper-cased
        self.request.sendall(_data.upper())
        pass
    pass


class Server:

    pass


def main():
    HOST, PORT = "0.0.0.0", 1081

    # Create the server, binding to localhost on port 1081
    server = socketserver.TCPServer((HOST, PORT), TcpServerHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    pass


if __name__ == '__main__':
    main()
    pass
