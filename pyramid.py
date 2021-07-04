def down():
    for b in range(10):
        for i in range(b + 1):
            print("*", end = '')
        print()

def up():
    for b in range(10):
        for i in range(10 - b):
            print("*", end = '')
        print()

def pyramid():
    for a in range(10):
        for c in range(10 - a):
            print(' ', end='')
        for b in range(2 * a + 1):
            print("*", end='')
        print()

def reversePy():
    for a in range(11):
        for c in range(a):
            print(' ', end='')
        for b in range(20 - (2 * a - 1)):
            print("*", end='')
        print()
    
def diamond():
    pyramid()
    reversePy()

diamond()
