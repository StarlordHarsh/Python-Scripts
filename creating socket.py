import socket
import sys
try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error , e:
    print ("Error occured"+e)
    sys.exit()
print ("Success")