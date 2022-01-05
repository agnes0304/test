import socket

cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cSocket.connect(('127.0.0.1', 1111))

# 사용자 인풋으로 채팅 받고 안 닫기/ 내가 socket close라고 쳐야 닫는거.

while True:
    l = input()
    if l != "exit":
        cSocket.send(l.encode('utf-8'))

        # message = cSocket.recv(4096)
        # if message:
        #     print(message.decode('utf-8'))

    else: 
        cSocket.send("exit".encode('utf-8'))
        cSocket.close()
        break