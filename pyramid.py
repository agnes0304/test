def down():
    for b in range(10):
        for i in range(b + 1):
            print("*", end='')
        print()


def up():
    for b in range(10):
        for i in range(10 - b):
            print("*", end='')
        print()


N = int(input()) // 2

def pyramid():
    for a in range(N):
        for c in range(N - a):
            print(' ', end='')
        for b in range(2 * a + 1):
            print("*", end='')
        print()


def reversePy():
    for a in range(N + 1):
        for c in range(a):
            print(' ', end='')
        for b in range(N * 2 - (2 * a - 1)):
            print("*", end='')
        print()


def diamond():
    pyramid()
    reversePy()


diamond()
