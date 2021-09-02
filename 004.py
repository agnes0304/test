# 004.1
# find 함수. 리스트 안에서 특정 숫자를 찾아내는 return 값은 찾고자 하는 원소의 index. 사용자 입력값
# 예를 들어 6을 찾고 싶어, 그럼 6이 몇번째에 있는지. 중복값은 가장 먼저 나오는 값의 자릿수. 
# 6이 들어왔어. 그럼 리스트의 0번째 부터 리스트 길이의 -1번째까지 맞는지 확인해야겠지. 
# 그리고 그게 맞으면 리턴.

# range 안에 들어가는 숫자는 알아서 -1.

# N = int(input())

def find(N):
    for i in range(len(f)):
        if N == f[i]:
            return f'{N}은 {i}번째에 있습니다.'
    return f'{N}은 리스트에 없습니다.'

# 중복값일 경우 자릿수 전부 출력

def find(N):
    temp = list()
    for i in range(len(f)):
        if N == f[i]:
            temp.append(i)
    return temp


# 004.2
# 인풋 N값을 전부 -1로.

def findCHANGE(N):
    for i in range(len(f)):
        if N == f[i]:
            f[i] = -1
    return f


# 004.3
# 인풋값을 전부 제거하고 새 리스트로.

def findDELETE(N):
    n = list()
    for i in range(len(f)):
        if N != f[i]:
            n.append(f[i])
    return n

# 004.4
# (index, number) index번째에 number 넣기
f = [10, 6, 9, 2, 3, 5, 6, 6 ,7, 8, 5, 6, 2, 16, 6]
# s = int(input())

def insert(s, N):
    return f[:s-1] + [N] + f[s:]


# 004.5
# 두개의 리스트를 combine, 위에 문법 안쓰고

o=[1,2,3]
m=[4,5,6]

def combine():
    for i in m:
        o.append(i)
    return o

def combineshort():
    return o + m

# 004.plus
# 1-T까지 전부 더한 값 반환. 
# 등차수열과 등비수열 일반항 알아두기.

T=int(input())
def trauma(T):
    return (T*(1 + T)) / 2

print(int(trauma(T)))
