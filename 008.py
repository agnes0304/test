# 008.1
# 100개의 랜덤한 정수값을 가진 리스트를 만들어봐라

import random
from typing import List

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
# 아놔 모르겠는데
# 내가 비교할거를 앞에서부터 비교해서 맞는자리에 끼워넣는거야. 2번은 1번, 3번은 1,2번, 4번은 1,2,3번
# 내가 비교할 애가 i면 i-1번 비교해야 함. 

agnes = [70, 80, 10, 3, 54, 1, 30, 99, 21, 65, 47]

def insertion(r, od):
    od = od.lower()

    if od != "asc" and od != "desc":
        print("asc/desc 중에 하나만 입력")

    for i in range(len(r)):
        for j in range(i+1):
            if od == "desc" and r[i] > r[j]:
                r[i], r[j] = r[j], r[i]
            elif od == "asc" and r[i] < r[j]:
                r[i], r[j] = r[j], r[i]
    return r

# insertion을 생각하고 작성하긴 했는데 실제 insertion인지...코드가 bubble sort랑 너무 비슷해서..
# print(insertion(agnes, "asc"))


# 008.6
# 퀵
# pivot기준으로 나눠. pivot보다 작은거, pivot, pivot보다 큰거. 
# 그놈의 recursive.
# 일단 랜덤으로 피봇이 정해지고 새 리스트가 있어. 
# 그 리스트에 맨 처음부터 비교를 해서 피봇보다 작은거 부터 append를 해. 

agnes = [70, 80, 10, 3, 54, 1, 30, 99, 21, 65, 47]



# 008.7
# dashlane, PW generator 만들어
# 사용자가 length, digit, letters, symbols 인풋으로. 
# 아 아스키 그냥 그 테이블에서 선택못하나.

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
        i = length//2
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


def dashlane_new(length, dig=True, lets=True, sym=True):
    pw_temp = list()
    if dig == True and lets == True and sym == True:
        pass


import string

# print(string.punctuation)


# 008.8

class Stack(List):
    def __init__(self):
        self = list()

    def isEmpty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.append(item)

    def pop(self):
        if len(self) != 0:
            temp = self[-1]
            self = self[:-1]
            return temp
        else:
            print("Empty stack")

    def peek(self):
        if len(self) != 0:
            print(self[-1])
        else:
            print("Empty stack")

    def size(self):
        return len(self)

a = Stack()
a.push(2)
print(a)