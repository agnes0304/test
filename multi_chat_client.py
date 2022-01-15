import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 1111))
while True:
    l = input()
    if l != "exit":
        c.send(l.encode('utf-8'))

        message = c.recv(4096)
        if message:
            print(message.decode('utf-8'))

    else: 
        c.send("exit".encode('utf-8'))
        c.close()
        break