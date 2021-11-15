# 007.7
# def makeMatrix(M: int, N: int, raw: str):
# 문자열 raw가 주어지면 M x N의 2차원 배열을 반환하는 함수 makeMatrix를 작성하세요.
# M = 4, N = 2, raw = "testtext"
# result = [["t", "e"], ["s", "t"], ["t", "e"], ["x", "t"]]

def makeMatrix(M, N, raw):
    matrix = list()
    for i in range(M):
        temp = list()
        for j in range(N):
            temp.append(raw[j + (i * 2)])
        matrix.append(temp)

    return matrix

print(makeMatrix(4,2,"testtext"))


# 5*5 크기의 2차원 배열 선언, 모두 0으로 넣자.
# 리스트가 계속 선언되면서 큰 리스트에 불어야겠지. 
def Matrix(M,N,n):
    a = list()
    for i in range(M):
        temp = list()
        for j in range(N):
            temp.append(n)
        a.append(temp)
    return a

# print(Matrix(5, 5, 0))
 

# 100*100 , 모두 -1
# print(Matrix(100,100,-1))


# target number를 찾는 함수, find Number를 만들자. 
# -1을 찾아야 하면 함수는 2,2를 출력. 

mtx = [[11, 12, 5, 2], [15, 6, 10], [10, 8, -1, 5], [12,15,8,6]]

def findNumber(t):
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j] == t:
                print(i, j)
                break
            else: 
                pass

# print(findNumber(-1))
# none 나오는 이슈 해결


# (N,M)에 있는 element 반환하는 access작성. 
# access(3,3) -> 6 
def access(N, M):
    print(mtx[N][M])

# access(3,3)


# 짝수를 만나면 전부 +1해서 홀수로.
def even2odd():
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j]%2 == 0 :
                mtx[i][j] = mtx[i][j] + 1
            else: 
                pass
    return mtx    

# print(even2odd())


# 10 이상의 숫자는 전부 0으로. 
def change0():
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j] >= 10 : 
                mtx[i][j] = 0
            else:
                pass
    return mtx

# print(change0())