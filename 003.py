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
          print("범위에 맞는 값을 넣으세요")
     else:
          temp = s[n-1]
          s[n-1] = s[m-1]
          s[m-1] = temp
          print(s)

# swap(s,n,m)

# 003.3 과제
# 두개로 분리하는 함수를 만들어라. N번째 원소 기준으로 리스트를 분리.

p = [5,10,15,6,11,55,77]
# N = int(input())

def split(p, N):
     left=list()
     right=list()
     left = p[:N-1]
     right = p[N-1:]
     print(left, right)
     

# split(p,N)


# 003.4 과제
# N번째 원소보다 작으면 less리스트, 크면 greater리스트로

# N이 5면, 실제 리스트에서는 4, o[4] 이 값이랑 리스트의 모든 값을 비교.

o=[5, 10, 15, 6, 11, 55, 77]
# N=int(input())

def sort(o, N):
     less=list()
     greater=list()
     for i in range(len(o)):
          if o[i] < o[N-1]:
               less.append(o[i])
          elif o[i] > o[N-1]:
               greater.append(o[i])
     print(less, greater)

#sort(o,N)

# 003.5 과제
# 뒤집기
# 주어진 리스트가 [5, 10, 15, 6, 11, 55, 77] reverse 함수에 리스트를 전달하고 나면 [77, 55, 11, 6, 15, 10, 5]
# 새로운 리스트 공간을 할당하지 않고 in-place로 해결 해야 합니다. 메모리를 아끼세요.

# 리스트의 첫번째와 마지막, 두번째와 마지막에서 두번째, 세번째와 마지막에서 세번째를 바꾸고, 네번째와 마지막에서 네번째를 바꿔
# 마지막은 리스트가 지금 7개면 3번째, 8개면 4번째까지만, 즉 리스트 원소 개수의 절반만 해주면 돼. 홀수개일 경우 2로 나눴을때의 몫
# 계속 바뀌는 건 i, i는 근데 리스트 원소개수의 절반. 

r = [5, 10, 15, 6, 11, 55, 77]

def reverse(r):
     for i in range(len(r)//2):
          t = r[len(r)-1-i]
          e = r[i]
          r[i] = t
          r[len(r)-1-i]=e
     return(r)

print(reverse(r))