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
    if od != "asc":
        if od != "dsc":
            print("asc/dsc 중에 하나를 입력하세요")
        else:
            for i in range(len(r)-1):   # 비교하는 횟수 하나씩 줄일라고 쓴거야
                for j in range(len(r)-1-i):
                    if r[j] > r[j+1]:
                        r[j], r[j+1] = r[j+1], r[j]
            r.reverse()
    elif od == "asc":
        for i in range(len(r)-1):
            for j in range(len(r)-1-i):
                if r[j] > r[j+1]:
                    r[j], r[j+1] = r[j+1], r[j]

    return r

# print(bubble(agnes, "sc"))


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

r = makerandomlist(100000)
start = time.time()
targetfind(r, 100)
end = time.time()
print(f"{end-start:.5f}초")
