import socket
import sys

TCP_IP="127.0.0.1"
TCP_PORT=8090
BUFFER_SIZE=1024
MESSAGE_TO_SERVER="Hello world"

try:
    tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print ("error"+e)
    sys.exit()

tcp_socket.connect((TCP_IP, TCP_PORT))

try:
    tcp_socket.send(MESSAGE_TO_SERVER)
except socket.error, e:
    print"Error"+e
    sys.exit()
print "Message send"