def down():
    for b in range(10):
        for i in range(b + 1):
            print("*", end='')
        print("")

def up():
    for b in range(10):
        for i in range(10 - b):
            print("*", end='')
        print("")

