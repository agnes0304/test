import random

class Subject:

    def __init__(self, title : str, score : int):
        self.title = title
        self.score = score 


class Student:

    def __init__(self, name: str):
        self.name = name
        self.id = random.randrange(2000,2021)
        self.subjects = []

    def addSubject(self, s: Subject):
        self.subjects.append(s)