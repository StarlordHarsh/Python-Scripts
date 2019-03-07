import socket
import sys
from thread import *

tcpip="127.0.0.1"
tcpport=8090
buff=1024

try:
    tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print "Error"+e
    sys.exit()
tcp_socket.bind((tcpip,tcpport))
tcp_socket.listen(2)
print "Listening"

def ClienConnectionHandler(connection):
    BUFFER=1024
    connection.send("Welcome to the server")

    while True:
        data = connection.recv(BUFFER)
        reply = "Data received:"+data
        if not data:
            break
        try:
            print("Message-" + data)
            connection.sendall(reply)
        except socket.gaierror,g:
            print(g)

    connection.close()

while True:
    connection, address = tcp_socket.accept()
    print ("Client connected:",address)
    start_new_thread(ClienConnectionHandler, (connection,))

tcp_socket.close()