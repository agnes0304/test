# 006. 주어진 str을 반복문을 통해 출력하되, 공백은 출력하지 않는 함수를 만들자

test = "jiwoo is the best"
# 띄어쓰기가 없어야 되는거고. 

# 여기서 변수가 테스트인거지. 끈 따옴표로 묶으면 변수가 아니라 상수인데
# 메모리에 공간을 할당하고 여기 엑세스를 하려면 이름이 필요한데 그게 테스트이다. test는 주소를 포인트하고 있는 거지
# 공간이 연속적으로 필요한건 리스트잖아. 문자열도 마찬가지로 연속적인 메모리 공간에 캐릭터들이 들어가있는거지 

# pass 대신에 continue. pass는 아무것도 하지말고 넘겨라. 필요 X

# 테스트의 0번째부터 쭉 돌면서 그 자리에 공백이 아니면 프린트, 공백이면 그냥 패스. 다음 자리수로 넘어가게 하는거. 테스트 길이만큼. 

def nospace(s):
    for i in range(len(s)):
        if s[i] != ' ' :
            print(s[i])


# 006.1
# s1 = "jiwooo" , s2 = "babooo" > s3 = "jbiawboooo" 합치는 함수! 
# 두 문자열 len은 같다

s1 = "jiwooo"
s2 = "babooo"

def mixv1():
    s3 = ''
    for i in range(len(s1)):
        s3 = s3 + s1[i] + s2[i]
    return s3


# 006.2
# 두개의 str길이가 다르면, mix할 수 있는 데까지 mix하고 남는 str은 맨뒤에 붙이고.
# mixv2

s4 = "sentiment"
s5 = "classification"

# 둘중에 길이짧은거 체크, 그 길이 만큼 print. 나머지는 긴거에서 길이 빼기 짧은 길이 그냥 붙이기.

def mixv2():
    s6 = ''
    if len(s4) < len(s5):
        for i in range(len(s4)):
            s6 = s6 + s4[i] + s5[i]
        s6 = s6 + s5[len(s4):]
        return s6
    elif len(s5) < len(s4):
        for i in range(len(s5)):
            s6 = s6 + s4[i] + s5[i]
        s6 = s6 + s4[len(s5):]
        return s6
    else:
        for i in range(len(s4)):
            s6 = s6 + s4[i] + s5[i]
        return s6


# 006.3
# ctrl +f 기능. 스트링을 주는데 거기서 원하는 뉴스 기사 내용 중에서 "A"를 찾아라 하면 그거 찾아서.
# 인덱스를 반환하자. 
# passage 단어 찾고 있으면 true. 없으면 false

# P로 시작하는 구간을 찾고 거기서 검증. 그거 반복. 

w = "jiwoo"
sample = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like). There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32."

def wfind():
    for i in range(len(sample)):
        if sample[i] == w[0]:
            w1 = str()
            for a in range(len(w)):
                w1 = w1 + sample[i + a]

            if w1 == w:
                return True

    return False
            
print(wfind())