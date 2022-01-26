# socket create - bind - listen - accpet - read - write - read(eof) - close

import socket
import threading

sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sv.bind(('127.0.0.1', 10000))
sv.listen()

# client마다 X/ 기능별 thread

clients = []


def broadcast(message, me):
    # send to all clients
    for c in clients:
        if c != me:
            c.send(message)

def handler(cs, addr):
    while True:
        message = cs.recv(4096)
        if message == b"exit":
            print(f'{addr} out')
            clients.remove(cs)
            cs.close()
            return

        print(message)
        broadcast(message, cs)

# accept c1 - 'c1 connected'print - append c1 clients[] - recv c1 message - thread t1 start
# thread; handler(print c1 msg - func broadcast())

while True:
    c, addr = sv.accept()
    print(f"{addr} has been connected")
    clients.append(c)

    t = threading.Thread(target=handler, args=(c, addr))
    t.start()

sv.close()
