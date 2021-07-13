nums = [3, 4, 1, 2, 30, 50, 90]

b = list()
c = list()


def makeOddorNotlist():
    for a in range(len(nums)):
        if nums[a] % 2:
            c.append(nums[a])
        else:
            b.append(nums[a])
    print(b)
    print(c)


# makeOddorNotlist()


#b = list()
# N = int(input())


def generateOdd(N):
    for a in range(N):
        if a % 2:
            b.append(a)
    print(b)


# generateOdd(N)


#N = int(input())

def generatePrimenumber(N):
    i = list()
    for a in range(2, N + 1):
        flag = True
        for b in range(2, a):
            if a % b == 0:
                flag = False
                break
        if flag:
            i.append(a)
    return i


#print(generatePrimenumber(N))


N=int(input())

def reverselist(N):
    x=list()
    for i in range(N):
        x.append(N-i)
    return x

reverselist(N)
print(reverselist(N))




Test = [5,4,3,2,1]

#n=int(input())

def remove(a, n):
    a[n-1]=-1
    

case = [6,7,8,10]

#remove(case, n)
#print(case)
