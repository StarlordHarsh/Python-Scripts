import socket

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

connection,address=tcp_socket.accept()
print "Connect with-", address

