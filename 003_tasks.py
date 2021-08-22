#print(reverselist_remove_2(N, M))
# 003.1 과제
# 0은 A로, 1은 B로 바꿔서 인코딩하는 함수. 치환불가 수는 error.
# abcdefghijklmnopqrstuvwxyz(25)

b = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
a = [20, 1, 1, 123]

# 리스트 a에 있는 요소가 리스트 B의 자리값의 알파벳을 불러오면 됨.

a = [0, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 9, 10, 100, 123123, 222, 1, 1, 2, 2]
a = [9, 8, 22, 14, 14]
a = [8, 13, 19, 9]

#for i in range(len(a)):
#     if a[i] < 26:
#          print(b[a[i]], end=' ')
#     elif a[i] >= 26:
#           print("error", end=' ')



# 003.2 과제
# 리스트 안의 원소 자리를 바꾸는 함수 swap()을 작성. 


s=[5,10,15,6,11,55,77]

#n=int(input())
#m=int(input())

def swap(s, n, m):
     if n >= len(s) or n < 0 or m >=len(s) or m < 0:
          print("저기요, 범위에 맞는 값을 넣으세여")
     else:
          temp = s[n-1]
          s[n-1] = s[m-1]
          s[m-1] = temp
          print(s)

# swap(s,n,m)

# 003.3 과제
# 두개로 분리하는 함수를 만들어라. N번째 원소 기준으로 리스트를 분리.

p = [5,10,15,6,11,55,77]
N = int(input())

def split(p, N):
     left=list()
     right=list()
     left = p[:N-1]
     right = p[N-1:]
     print(left, right)
     

split(p,N)


