# 소켓 socket 만들기(서버)-bind-listen-accept
# read
# client close read, close

import socket

svSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svSocket.bind(('127.0.0.1', 1111))

svSocket.listen()


while True:
    cSocket, addr = svSocket.accept()
    print(addr)
    
    while True:
        message = cSocket.recv(4096)
        print(message)

        if message == b"exit":
            cSocket.close()
            break

svSocket.close()
