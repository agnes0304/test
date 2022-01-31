# 005 과제
# 아래와 같은 2차원 리스트가 주어질 때, 다음과 같이 출력하는 함수 작성
# [0][0~N]있으면 출력하고 없으면 바로 앞에 []이 안에 1이 들어가. 또 그렇게 하고 [2]들어가
# 언제까지 반복? test라는 리스트의 길이-1만큼(어차피 range 쓰면 -1되니까 그냥 길이만 넣고)

test = [[0,1,2], [3,4,5], [6,7,8]]
# print(len(test))하니까 3나옴. 
# print(len(test[0]))하니까 3나옴

def twoDarray():
    for d in range(len(test)):
        for i in range(len(test[d])):
            print(test[d][i], end=' ')
        print()

# twoDarray()