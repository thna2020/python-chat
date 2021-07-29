import socket
import sys
import time

### init ###

s = socket.socket()
host = socket.gethostname()
print('Server will start on host:', host)
port = 8080
s.bind((host, port))
print()
print('Server successfully binds to host and port.\n')
print('Server is waiting for incoming connection(s).\n')
s.listen(1)
conn, addr = s.accept()
print(addr, 'has connected to server and is now online.\n')

while 1:
    message = input(str('>> '))
    message = message.encode()
    conn.send(message)
    print('Message has been sent.\n')
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print('Client:', incoming_message)
    print()