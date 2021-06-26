x = "*"

def star():
    for a in range(1,11):
        print(x)

for b in range(10):
    for i in range(b + 1):
        print("*", end='')
    print("")

for b in range(10):
    for i in range(10 - b):
        print("*", end='')
    print("")

