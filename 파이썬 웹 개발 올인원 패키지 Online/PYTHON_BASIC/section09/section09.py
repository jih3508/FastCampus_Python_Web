# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# .. : 상대경로, . : 절대 경로

# 파일 읽기
# 예제1
f = open('./section09/resource/review.txt', 'r')
content = f.read()
print(content)

# 반드시 close 리소스 반환
f.close()

# 예제2
# with문 사용시 close 사용 할 필요 없다.
with open('./section09/resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("---------------------------------------------------")

# 예제3
with open('./section09/resource/review.txt', 'r') as f:
    for c in f:
        print(c)

print("---------------------------------------------------")

# 예제4
with open('./section09/resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용 없음
    print(">", content)

print("---------------------------------------------------")

# 예제5
with open('./section09/resource/review.txt', 'r') as f:
    line = f.readline() # 한줄식 읽어 온다.
    #print(line)
    while line:
        print(line, end='> ')
        line = f.readline()

print("---------------------------------------------------")

# 예제6
with open('./section09/resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end='> ')

print("---------------------------------------------------")

# 예제7
with open('./section09/resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제1
with open('./section09/resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')

with open('./section09/resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')

# 예제3
from random import randint

with open('./section09/resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 45)))
        f.write('\n')

# 예제4
# writelines : 리스트 → 파일로 저장
with open('./section09/resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

# 예제5
with open('./section09/resource/text4.txt', 'w') as f:
    print('Test Contensts1!', file=f)
    print('Test Contensts2!', file=f)