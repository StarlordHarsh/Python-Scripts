import SocketServer

class TCPrequestHandler (SocketServer.StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print '{} wrote:'.format(self.client_address[0])
        print self.data
        self.request.sendall(self.data)

    server = SocketServer.TCPServer(("",8090), TCPrequestHandler)
    server.serve_forever()