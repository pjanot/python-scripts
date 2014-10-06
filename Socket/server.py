# Echo server program
import socket
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    time.sleep(1)
    print 'receiving'
    data = conn.recv(1024)
    print 'done'
    if data:
        print 'sending back'
        conn.sendall('Hello ' + data)
        print 'done'
    else:
        print 'waiting'
conn.close()
