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

for i in range(len(a)):
     if a[i] < 26:
          print(b[a[i]], end=' ')
     elif a[i] >= 26:
          print("error", end=' ')


