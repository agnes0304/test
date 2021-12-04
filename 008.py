# 008.1
# 100개의 랜덤한 정수값을 가진 리스트를 만들어봐라

import random

def makerandomlist(n):
    r = list()
    for i in range(n):
        i = random.randrange(1, 1000)
        r.append(i)

    return r


# 008.2
# def bubble(input, order):
# 입력으로 리스트를 주면, 정렬된 리스트를 돌려주는 버블 소트 함수를 작성하세요.
# 단 함수는 오름차순, 내림차순 모두 가능해야 합니다 따라서.
# order 파라미터를 통해 오름차순, 내림차순을 조절 할 수 있도록 하세요

# 리스트를 받아, if 오름차순이면 전자와 후자 비교, 전자가 크면 스왑. 그리고 i가 옆으로 넘어가게.
# if 내림차순이면, 전 후 비교, 전자가 작으면 스왑. 
# 근데 일단 스왑하고 리버스 하는게 빠른가 아님 처음부터 조건을 다르게 설정하는게 나은가. 

agnes = [70, 80, 10, 3, 54, 1, 30, 99, 21, 65, 47]

def bubble(r, od):
    od = od.lower()

    if od != "asc" and od != "desc":
            print("asc/desc 중에 하나를 입력하세요")
    
    for i in range(len(r)-1):   # 비교하는 횟수 하나씩 줄일라고 쓴거야
        for j in range(len(r)-1-i):
            if od == "asc" and r[j] > r[j+1]:
                r[j], r[j+1] = r[j+1], r[j]
            elif od == "desc" and r[j] < r[j+1]:
                r[j], r[j+1] = r[j+1], r[j]

    return r

# print(bubble(agnes, "asc"))


# 008.3
# 위에서 구현한 bubble 정렬 함수에 입력으로 정수 십만개를 가진 리스트를 넣어서 실행 한 뒤 코드의 실행 시간을 측정 해 보세요.

import time

def measuretime():
    start = time.time()
    bubble(agnes, "asc")
    end = time.time()

    print(f"{end-start:.5f}초")


# 008.4
# 먼저 정수 랜덤 리스트 십만개를 만듭니다.
# target number를 찾는 함수 find를 만드세요.
# 함수는 1초안에 결과 값을 return 해야 합니다.

def targetfind(r, t):
    for i in range(len(r)):
        if r[i] == t:
            print(i+1, "번째에 있음")

# r = makerandomlist(100000)
# start = time.time()
# targetfind(r, 100)
# end = time.time()
# print(f"{end-start:.5f}초")


# 008.5
# insertion sort 
# 80을 70이랑 비교하고, 10을 80, 70이랑 비교하고, 3을 80, 70, 10이랑 비교하고, 54를 80, 70, 10, 3이랑 비교하고
# 1번은 0
# 2번은 1,0
# 3번은 2,1,0
# 4번은 3,2,1,0
# 루프도는 건 앞에서. 비교하는건 역순으로?

test = [70, 80, 10, 3, 54, 62, 32, 30]

def insertion(raw):
    for i in range(len(raw)):   # i는 0,1,2,3,4
        for j in range(i, 0, -1):
            if raw[j] < raw[j-1]:
                raw[j], raw[j-1] = raw[j-1], raw[j]
    return raw

print(insertion(test))

# 008.6
# 퀵
# pivot기준으로 나눠. pivot보다 작은거, pivot, pivot보다 큰거. 
# recursive.
# 일단 랜덤으로 피봇이 정해지고 새 리스트가 있어. 
# 그 리스트에 맨 처음부터 비교를 해서 피봇보다 작은거 부터 append를 해. 

agnes = [70, 80, 10, 3, 54, 1, 30, 99, 21, 65, 47]



# 008.7
# dashlane, PW generator 만들어
# 사용자가 length, digit, letters, symbols 인풋으로. 

def dashlane_old(length, dig=True, let=True, sym=True):
    pw_temp = list()
    digit = ['0','1','2','3','4','5','6','7','8','9']
    
    letters = list()

    for i in range(65, 91):
        letters.append(chr(i))
    for i in range(97, 123):
        letters.append(chr(i))

    symbols = list()
    for i in range(33, 48):
        symbols.append(chr(i))
    for i in range(58, 65):
        symbols.append(chr(i))
    for i in range(91, 97):
        symbols.append(chr(i))
    for i in range(123, 127):
        symbols.append(chr(i))


    if dig == True and let == True and sym == True:
        i = length // 3
        r = length % 3

        for _ in range(i):
            pw_temp.append(random.choice(digit))
        
        for _ in range(i):
            pw_temp.append(random.choice(letters))

        for _ in range(i+r):
            pw_temp.append(random.choice(symbols))

    elif dig == True and let == True:
        i = length // 2
        r = length % 2

        for _ in range(i):
            pw_temp.append(random.choice(digit))

        for _ in range(i+r):
            pw_temp.append(random.choice(letters))


    elif dig == True and sym == True:
        i = length // 2
        r = length % 2

        for _ in range(i):
            pw_temp.append(random.choice(digit))

        for _ in range(i+r):
            pw_temp.append(random.choice(symbols))
    

    elif let == True and sym == True:
        i = length//2
        r = length % 2

        for _ in range(i):
            pw_temp.append(random.choice(letters))

        for _ in range(r+i):
            pw_temp.append(random.choice(symbols))

    else:
        print("length 이후엔 True/False를 각각 입력, 최소 2개 이상 True")
    
    random.shuffle(pw_temp)

    pw = str()
    for i in range(len(pw_temp)):
        pw += pw_temp[i]

    print(pw)


import string

def dashlane_new(length : int, dig : bool, lets : bool, sym : bool):
    result = str()
    while len(result) <= length:
        if dig:
            # 옵션 on/off 참고
            result += random.choice(string.digits)
        if lets:
            result += random.choice(string.ascii_letters)
        if sym:
            result += random.choice(string.punctuation)

    return result[:length]


# 008.8
# self는 키워드라서 변수 다른걸로 선언해야 함. 

class Stack():
    def __init__(self):
        self.stack = list()
        self.n = 0

    def isEmpty(self) -> bool:
        return not self.n

    def push(self, item):
        self.stack.append(item)
        self.n += 1

    def pop(self):
        if self.n != 0:
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
            self.n -= 1
            return temp
        else:
            print("Empty stack")

    def peek(self):
        if self.n != 0:
            print(self.stack[-1])
        else:
            print("Empty stack")

    def size(self):
        return self.n



# 008.9
# size랑 empty판별 위한 게 필요

class Queue:
    def __init__(self):
        self.queue = []
        self.n = 0

    def isEmpty(self):
        if self.n == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        self.queue.append(item)
        self.n += 1

    def dequeue(self):
        if self.n != 0:
            temp = self.queue[0]
            self.n -= 1
            self.queue = self.queue[1:]
            return temp
        else: 
            print("Empty Queue")

    def size(self):
        return self.n

    def __str__(self):
        return "나만의 출력 " + str(self.queue)


# q = Queue()
# q.enqueue("4")
# q.enqueue("3")
# q.enqueue("2")
# q.enqueue("1")

# test = list()

# print(q)
# 이전 버전에서 q.queue이렇게 했는데 원래 직접 접근하면 안 된다.
# 클래스 내부에 queue 없으면 생겨버리는 상황 발생. 


# 008.10
# Student 클래스(각 학생은 이름, 학번, 국,영,수 점수가짐)
# avg() 함수는 국영수 점수의 평균을 반환.
# sum() 함수는 국영수 점수의 합을 반환.
# Student 10명을 랜덤으로 만든 다음 평균 점수가 높은 학생 순으로 정렬.


class Student:
    def __init__(self, name, code, kor, eng, math):
        self.name = name
        self.code = code
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        self.s = self.kor + self.eng + self.math

    def avg(self):
        self.a = (self.kor + self.eng + self.math) / 3
        return self.a

students = []
for i in range(10):
    a = Student("wldn{}".format(i) , random.randrange(2000, 2021), random.randrange(1, 100), random.randrange(1, 100), random.randrange(1, 100))
    students.append(a)
# print(students)

for i in range(len(students)-1):
    for j in range(len(students)-1-i):
        if students[i].avg() < students[i+1].avg():
            students[i], students[i+1] = students[i+1], students[i]
# print(students)


# 008.11
# linked list의 노드 클래스 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
