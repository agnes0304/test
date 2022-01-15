# socket create - bind - listen - accpet - read - write - read(eof) - close

import socket
import threading

sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sv.bind(('127.0.0.1', 1111))
sv.listen()

# client마다 X/ 기능별 thread

clients = []

def broadcast(message):
    # send to all clients
    for c in clients:
        c.send(message)

    if message == b"exit":
        clients.remove(c)
        c.close()

def handler(c):
    print("thread", id)
    while True:
        print(message)
        broadcast(message)

# accept c1 - 'c1 connected'print - append c1 clients[] - recv c1 message - thread t1 start
# thread; handler(print'thread id' - print c1 msg - func broadcast())

while True:
    c, addr = sv.accept()
    print(f"{addr} has been connected")
    clients.append(c)

    message = c.recv(4096)

    t = threading.Thread(target=handler, args=(message))
    t.start()

sv.close()
