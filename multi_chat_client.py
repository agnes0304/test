import socket
import threading

# sv 에서 broadcast 듣기/ msg sending

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 10000))
signal = False


def listener(c):
    while True and not signal:
        message = c.recv(4096)
        if message:
            print(message.decode('utf-8'))


t = threading.Thread(target=listener, args=(c,))
t.start()


while True:
    l = input()
    if l != "exit":
        c.send(l.encode('utf-8'))
    else:
        signal = True
        c.send("exit".encode('utf-8'))
        break
