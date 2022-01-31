# 버블소팅

# 0번과 1번 비교, 0번이 1번보다 크면 1번으로, 그렇지 않은 경우는 1번과 2번 비교.
# 한번 회전할때마다 가장 마지막 거랑은 비교가 되면 안돼. 1회전때는 len-2. 2회전때는 len-3이어야 하고
# n회전때는 len-(n+1)이어야 하는데

r = [77, 55, 11, 6, 15, 10, 5]

def sortasc(r):
    for n in range(len(r)-1):
        for i in range(len(r)-(n+1)):
            if r[i] > r[i+1]:
                r[i], r[i+1] = r[i+1], r[i]
            else:
                pass
    return r

# 008.5부터 다른 sorting func 구현.