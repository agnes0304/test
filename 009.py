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

def agegroupFilter(ag : int):
    us_targetAge_all = []

    for i in range(len(us_py)):

        if us_py[i]['age'] >= ag and us_py[i]['age'] <= (ag + 9) :
            us_targetAge_all.append(us_py[i]) 

    return us_targetAge_all

print(agegroupFilter(20))