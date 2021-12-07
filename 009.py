# 009.03
# 입력으로 주어진 str이 몇번 등장하는지 count하는 함수


def countWord(word : str):
    count = 0
    fr = open("/Users/jiwoo/code/file.test/sample.txt", 'r')

    fr_a = fr.readlines()
    for i in range(len(fr_a)):
        fr_line = fr_a[i].split(' ')

        for i in range(len(fr_line)):
            if word == fr_line[i]:
                count += 1
    
    return count

# print(countWord("blandit"))


# 009.04
# 유저들의 정보를 20대 남/녀만 filtering 해 보세요.
# /Users/jiwoo/code/file.test/users.json

# "age" 20~29(agegroup)


import json

with open("/Users/jiwoo/code/file.test/users.json", 'r') as us_json:
    us_py = json.load(us_json)

# print(len(us_py))

def keypresent(i: int, k: str):
    
    keys = list(us_py[i].keys())

    for _ in range(len(keys)):
        if k in keys:
            return True
        else: 
            return False

# print(keypresent(0, "안녕"))
# 정상

count = 0
for i in range(len(us_py)):
    if keypresent(i, 'age') == True:
        count += 1
# print(count)

def agegroupFilter(ag : int):
    us_targetAge_all = []

    for i in range(len(us_py)):
        if keypresent(i, 'age') == True and us_py[i]['age'] >= ag and us_py[i]['age'] <= (ag + 9) :
            us_targetAge_all.append(us_py[i])

    return us_targetAge_all

print(len(agegroupFilter(10)))
print(len(agegroupFilter(20)))
print(len(agegroupFilter(30)))
print(len(agegroupFilter(40)))
print(len(agegroupFilter(50)))
print(len(agegroupFilter(60)))
print(len(agegroupFilter(70)))
print(len(agegroupFilter(80)))
print(len(agegroupFilter(90)))


# age 없는 애들 처리?