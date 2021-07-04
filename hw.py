def pyramid():
    for a in range(10):
        for c in range(10 - a):
            print(' ', end='')
        for b in range(2 * a + 1):
            print("*", end='')
        print()

pyramid()

def reversePy():
    for a in range(11):
        for c in range(a):
            print(' ', end='')
        for b in range(20 - (2 * a - 1)):
            print("*", end='')
        print()
    
reversePy()

