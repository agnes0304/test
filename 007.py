# 007
# str! immutable하다
# reversed = "oood ij eht fo yradnegel ehe oowiJ"

# 함수

test = "Jiwoo the legendary of the ji dooo"

# parameter로 t etc. 제대로 선언하도록.
# 함수 선언할 때 내가 인풋으로 뭘 넣을지 모르는 거잖아. 내가 t에 test라고만 해두면 test만 적용되는 함수인데 그럼 그게 함수겠니.
# 폰노이만 구조를 왜 처음에 설명했겠니.


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
        # 스트링에 이렇게 append하면 겁나 느리다. 왜? 계속 잡아서 늘이고 잡아서 늘이고.
        # 원래 그래서 이 방법은 아니다.

    return test3

# heap에 대해서.
# 처음부터 반복문을 거꾸로 읽으면서 스트링에 append하면 되는데 일단 리스트 공간 안 잡아도 되니까.
# for i in range(내가 읽을라는거, 0, -1)
# 아 과제. 업그레이드 하기(리스트 선언 안하는것)


# += 사용할 때 str 랑 list 차이
# append한 순간 공간 자체가 달라진거지. 다른 공간 잡은
# j = "string은 아직 나한테 좀 어려운듯."
# print(id(j))
# j += "근데 파이썬 자체 아직은...ㅋㅋㅋㅋ"
# print(id(j))
# 오 리스트는 주소값이 같음.
# 앞에 넣을 때나, 뒤에 넣을 때 다 달라.
# j = [1,2,3,4,5,6,7,8]
# print(id(j))
# j = [100] + j
# print(j)
# print(id(j))

# 이벤트를 해, 이름, 비번, 주소 등등 넣어, 한번에 백만개 온다고 해. 10일한다고 쳐.
# 입력폼의 메모리 사용량을 알고 있잖아. 직전에 그 폼을 예상해서 한 천만개 해놓고.
# preallocate해야 돼. 오....

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
            # 인덱스 에러나서 이것저것 해보다가 -1을 넣었는데 나옴. 근데 왜 -1을 해야 하는지 아직 이해하지 못함.
        else:
            templist.append(temp)
            temp = str()
    templist.append(temp)

    result = list()
    for i in range(len(templist), 0, -1):
        result.append(templist[i-1])
        # 인덱스 에러나서 이것저것 해보다가 -1을 넣었는데 나옴. 근데 왜 -1을 해야 하는지 아직 이해하지 못함.
    return result


# 007.5
# 2차원 배열 형태의 3x3 matrix로 mapping 시키는 함수
# matrix = [
#    ["A", "B", "C"],
#    ["D", "E", "F"], 
#    ["G", "H", "I"]
# ]

raw = "ABCDEFGHI"
def mapping33(r):
    matrix = list()
    m = list()

    for i in range(len(r)):
        m.append(r[i])

    matrix.append(m[:3])
    matrix.append(m[3:6])
    matrix.append(m[6:9])

    for i in range(len(matrix)):
        print(matrix[i], sep = '\n')

# 답은 잘 나오지만 틀린 것 같은데 뭐가 틀렸는지 모르겠음.
