# 009.03
# 입력으로 주어진 str이 몇번 등장하는지 count하는 함수


import student
import random
import json


def countWord(word: str):
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


with open("/Users/jiwoo/code/file.test/users.json", 'r') as us_json:
    us_py = json.load(us_json)

# print(len(us_py))
# 251


def agegroupFilter(ag: int):
    us_targetAge_all = []

    for i in range(len(us_py)):
        if us_py[i]['age'] >= ag and us_py[i]['age'] <= (ag + 9):
            us_targetAge_all.append(us_py[i])

    return us_targetAge_all

# print(len(agegroupFilter(10)))
# print(len(agegroupFilter(20)))
# print(len(agegroupFilter(30)))
# print(len(agegroupFilter(40)))
# print(len(agegroupFilter(50)))
# print(len(agegroupFilter(60)))
# print(len(agegroupFilter(70)))
# print(len(agegroupFilter(80)))
# print(len(agegroupFilter(90)))

# 009.05
# 008에서 만든 Student 클래스로 1000명의 학생을 만드세요.
# Student 클래스를 JSON 형태로 표현합니다.
# 1000명의 학생 정보를 file write해 json으로 저장합니다.


students = []

for i in range(1000):
    st = student.Student(f"최지우{i}")

    sb1 = student.Subject("KOR", random.randrange(1, 100))
    sb2 = student.Subject("ENG", random.randrange(1, 100))
    sb3 = student.Subject("MATH", random.randrange(1, 100))

    st.addSubject(sb1)
    st.addSubject(sb2)
    st.addSubject(sb3)

    students.append(st)


