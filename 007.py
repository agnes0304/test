# 007
# str! immutable하다
# reversed = "oood ij eht fo yradnegel ehe oowiJ"

# 함수

from typing import NewType

test = "Jiwoo the legendary of the ji dooo"

# parameter로 t etc. 제대로 선언하도록.
# 함수 선언할 때 내가 인풋으로 뭘 넣을지 모르는 거잖아. 내가 t에 test라고만 해두면 test만 적용되는 함수인데 그럼 그게 함수겠니.
# 폰노이만 구조!

def reversestr(t):

    # 리스트 길이 알고 있는 경우, 아래 방법처럼하면 GC 리스크 감소.
    # 0을 33개 있는 리스트 만들어서 거기에 t를 하나씩 주면 되는거.
    test2 = [0 for i in range(len(t))]

    for i in range(len(t)):
        test2[i] = t[i]
    #  test2 = ['J", ]....

    for i in range(len(test2) // 2):
        temp = test2[i]
        test2[i] = test2[len(test2) - 1 - i]
        test2[len(test2) - 1 - i] = temp

    # 데이터 타입만 다르잖아.
    test3 = str()
    for i in range(len(test2)):
        test3 += test2[i]
        # 스트링에 이렇게 append하면 느리다. 왜? 계속 잡아서 늘이고 잡아서 늘이고.
        # 원래 그래서 이 방법은 아니다.

    return test3

# heap에 대해서.
# 처음부터 반복문을 거꾸로 읽으면서 스트링에 append하면 되는데 일단 리스트 공간 안 잡아도 되니까.
# for i in range(내가 읽을라는거, 0, -1)
# 과제: 리스트 선언 없이 업그레이드


# += 사용할 때 str 랑 list 차이
# append한 순간 공간 자체가 달라진거지. 다른 공간 잡은
# j = "string..."
# print(id(j))
# j += "python..."
# print(id(j))
# 리스트는 주소값이 같음.
# 앞에 넣을 때나, 뒤에 넣을 때 다 달라.
# j = [1,2,3,4,5,6,7,8]
# print(id(j))
# j = [100] + j
# print(j)
# print(id(j))

# 이벤트를 해, 이름, 비번, 주소 등등 넣어, 한번에 백만개 온다고 해. 10일한다고 쳐.
# 입력폼의 메모리 사용량을 알고 있잖아. 직전에 그 폼을 예상해서 한 천만개 해놓고.
# preallocate해야 함. 


# 007.1
# case1의 결과 값으로 25를 반환하는 함수 calculator를 만드세요.
# case2 = "1*90/20"
# case3 = "327423+1293129-1"

# 일단 다 잘라. str을 int로 감싸면 그게 int로 바뀌긴 하지. 근데 연산자는? 

case0 = "1+2+3-5+1+1+1+1+1"

def calculator_1(c):
    temp_n = list() # 숫자 리스트
    temp_o = list() # 연산자 리스트
    for i in range(len(c)):
        if i % 2 == 0 :
            temp_n.append(c[i])
        else:
            temp_o.append(c[i])
    temp_n.reverse()
    temp_o.reverse()

    while temp_o: # tmep_o가 비어있기 전까지. (비어있으면 false)
        N = int(temp_n.pop())
        N2 = int(temp_n.pop())
        O = temp_o.pop()
        N3 = int()

        if O == '+':
            N3 = N + N2
            temp_n.append(N3)
        elif O == '-':
            N3 = N - N2
            temp_n.append(N3)
        

    print(temp_o, temp_n)
    print("result is ", temp_n.pop())


case1 = "1+2+30-8"
def calculator_2(c): 
    temp_n = list()
    temp_o = list()
    temp_s = str()

    for i in range(len(c)):
        if c[i].isdigit() == True:
            temp_s += c[i]
        else:
            temp_n.append(int(temp_s))
            temp_s = str()
            temp_o.append(c[i])
    
    temp_n.append(int(temp_s))

    temp_n.reverse()
    temp_o.reverse()

    while temp_o: # tmep_o가 비어있기 전까지. (비어있으면 false)
        N = int(temp_n.pop())
        N2 = int(temp_n.pop())
        O = temp_o.pop()
        N3 = int()

        if O == '+':
            N3 = N + N2
            temp_n.append(N3)
        elif O == '-':
            N3 = N - N2
            temp_n.append(N3)
        
    print(temp_o, temp_n)
    print("result is ", temp_n.pop())


# 007.2
# split 함수
# result = ["Jiwoo", "the", "legendary", "of", "the", "ji", "dooo"]

test = "Jiwoo the legendary of the ji dooo"

def string2list(t):
    temp = str()
    result = list()
    for i in range(len(t)):
        if t[i] != ' ':
            temp += t[i]
        else:
            result.append(temp)
            temp = str()
            # 초기화 과정
    # temp = "dooo"
    result.append(temp)
    return result


# 007.3

test = ["Jiwoo", "the", "legendary", "of", "the", "ji", "dooo"]

def list2string(t):
    result = str()
    for i in range(len(t)):
        if i == len(t) - 1:
            result += t[i]
        else: 
            result += t[i] + ' '
    print(result)


# 007.4
# test = ["oowiJ", "eht", "yradnegel", "fo", "eht", "ij", "oood"]

test = "Jiwoo the legendary of the ji dooo"

def string2reversedList(t):
    temp = str()
    templist = list()
    for i in range(len(t), 0, -1):
        if t[i-1] != ' ':
            temp += t[i-1]
            # 거꾸로 돌면 3,2,1,0이 아니라 4,3,2,1이다. 그래서 -1해줘야 함.
        else:
            templist.append(temp)
            temp = str()
    templist.append(temp)

    result = list()
    for i in range(len(templist), 0, -1):
        result.append(templist[i-1])
    return result


# 007.5
# 2차원 배열 형태의 3x3 matrix로 mapping 시키는 함수
# string의 길이는 항상 9라고 가정합니다.
# matrix = [
#    ["A", "B", "C"],
#    ["D", "E", "F"], 
#    ["G", "H", "I"]
# ]

raw = "ABCDEFGHI"
def mapping33(r):
    matrix = list()
    m1 = list()

    for i in range(len(r)):
        m1.append(r[i])

    matrix.append(m1[:3])
    matrix.append(m1[3:6])
    matrix.append(m1[6:9])

    return matrix


# 007.6 v1
# string의 길이는 항상 3의 배수라고 가정합니다.
# new_matrix = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"],~]

raw = "ABCDEFGHIJKL123ㅈㄷㄱ890ㅑㅐㅔ"
def mapping3n_v1(r):
    m2 = list()
    for i in range(len(r)):
        m2.append(r[i])

    new_matrix = list()
    for i in range(len(m2)):
        if m2[3*i:3*i+3] != list():
            new_matrix.append(m2[3*i:3*i+3])
    return new_matrix


# 007.6 v2.
# 1. 문자열을 하나 하나 반복한다
# 2. 3개 단위로 끊어서 리스트에 집어 넣음
# 3. 그 리스트를 다시 new_matrix 리스트에 집어넣는다

raw = "ABCDEFGHIJKL"
def mapping3n_v2(r):
    new_matrix2 = list()

    for i in range(len(r)//3):
        temp = list()
        # /는 정말 나누는거. 소수점으로 인식. //은 정수형으로 인식. 몫만 가지고 옴. 
        for j in range(3):
            temp.append(r[j + (i * 3)])
            # 인덱스로 접근한다는 생각을 해야함. 
        new_matrix2.append(temp)

    return new_matrix2

# i는 y축, j는 x축


# 나머지 문제들은 007_matrix.py에


# 007.8
case0 = "1+2+3-5"
case1 = "1+2+30-8"
case2 = "1*90/20"
case3 = "327423+1293129-1"

# 지난번에 다 완성하지 못한 계산기를 다시 만들기. 조건은 같음.
# 함수의 입력은 string이고 반환 타입은 int 입니다.
# 곱셉과 나눗셈의 연산자 우선순위는 고려하지 않아도 됩니다. 순서대로 계산하세요.

def cal(c):
    o = list()
    v = list()
    temp = str()

    for i in range(len(c)):
        if c[i].isdigit():
            temp += c[i]
        else:
            v.append(temp)
            temp = str()
            o.append(c[i])
    
    v.append(int(temp))

    v.reverse()
    o.reverse()
    
    while o:
        n1 = int(v.pop())
        n2 = int(v.pop())
        op = o.pop()
        n3 = int()
        
        if op == "+":
            n3 = n1 + n2
            v.append(n3)
        elif op == "-":
            n3 = n1 - n2
            v.append(n3)
        elif op == "/":
            n3 = n1/n2
            v.append(n3)
        elif op == "*":
            n3 = n1*n2
            v.append(n3)
        
    return int(v.pop())    

print(cal(case3))