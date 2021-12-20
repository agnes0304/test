import random


class Subject:

    def __init__(self, title: str, score: int):
        self.title = title
        self.score = score

    def __str__(self) -> str:
        return self.title


class Student:
    def __init__(self, name: str):
        self.name = name
        self.id = random.randrange(2000, 2021)
        self.subjects = []
        self.password = "123"

    def addSubject(self, s: Subject):
        self.subjects.append(s)

    # overloading
    def __str__(self) -> str:
        return f"{self.name} {self.id} {self.subjects[0]}"

    def __add__(self, other):
        return self.name + other.name


s1 = Student(name="최지우")
s2 = Student(name="유호민")

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(l1 + l2)
