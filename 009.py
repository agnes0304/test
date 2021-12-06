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

print(countWord("blandit"))