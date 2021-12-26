# 인스타그램 시스템 모방_클래스

# O2M
# class Post:
# class Comment:
# class User:

# Post 클래스: 글 쓰기(create), 글 내용 수정(update), 글 삭제(delete), 댓글 달기(addComment), 하트(heart)
# User 클래스 기능: Post 북마킹, 닉네임 변경, 내가 올린 포스트 목록 불러오기


from datetime import datetime


class Comment:
    def __init__(self, cmt):
        self.u_id = u_id
        self.comment = cmt
        self.time = datetime.now()


class User:
    def __init__(self, name : str, u_id: str, pw, birth, email: str):
        self.name = name
        self.u_id = u_id
        self.pw = pw
        self.birth = birth
        self.email = email
        self.bookmarks = []
        self.myposts = []
        self.blocking = []

    def changeName(self, new: str):
        self.name = new

    def bookmark(self, p_id):
        self.bookmarks.append(p_id)
    
    def block(self, u_id):
        self.blocking.append(u_id)

    def callmyPost(self):
        return self.myposts

    def create(self, cnt):
        newPost = Post(self.name + str(len(self.myposts) + 1), cnt)
        self.myposts.append(newPost)

    def delete(self, num: int):
        if num > len(self.myposts) or num < 0:
            print("No such post. You have" + len(self.myposts) + "posts.")
        else:
            del self.myposts[num - 1]

    def update(self, p_id, n_str):
        target = findPostById(p_id)
        target.cnt = n_str
        target.time = datetime.now()


class Post:
    def __init__(self, p_id: str, cnt):
        self.p_id = p_id
        self.contents = cnt
        self.time = datetime.now()
        self.heart = 0
        self.comments = []
        self.postlist = []

    def addComment(self, c: Comment):
        self.comments.append(c)
    

def findPostById(id: int) -> Post:
    return Post()

def addComment(frm: User, to: User, p_id: str, cmt: Comment):
    if frm not in to.blocking:
        for i in range(len(to.myposts)):
            if to.myposts[i].p_id == p_id:
                to.myposts[i].addComment(cmt)
    else: 
        print("You're blocked")

def addHeart(frm: User, to: User, p_id: str):
    if frm not in to.blocking:
        for i in range(len(to.myposts)):
            if to.myposts[i].p_id == p_id:
                to.myposts[i].heart += 1
    else: 
        print("You're blocked")

def bookmark(frm: User, to: User, p_id):
    if frm not in to.blocking:
        for i in range(len(to.myposts)):
            if to.myposts[i].p_id == p_id:
                frm.bookmark(p_id)
    else: 
        print("You're blocked")


u1=User("u1", "u1_id", "u1_pw", "19970304", "u1@gmail.com")
u2=User("u2", "u2_id", "u2_pw", "19970305", "u2@gmail.com")
u3=User("u3", "u3_id", "u3_pw", "19970306", "u3@gmail.com")

u1.changeName("J")
u2.changeName("H")
u3.changeName("M")

u1.block(u2)
print(u1.blocking)

u1.create("first post")
print(u1.myposts)
print(u1.myposts[0].p_id)

bookmark(u2,u1,'J1')
addHeart(u2,u1,"J1")
addComment(u3,u1,'J1', "good!")

print(u1.myposts[0].comments)