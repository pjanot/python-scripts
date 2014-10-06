# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def send_data(word):
    ret = s.sendall(word)
    print 'Sending', word, ret
    data = s.recv(1024)
    print 'Received', repr(data)

data_lines = ['colin', 'toto']
map(send_data, data_lines)
