# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서, 중복, 수정, 삭제)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])


# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()
print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.insert(2, 7)
print(y)
y.remove(7)
print(y)
y.pop()
print(y)
ex = [88, 77]
y.extend(ex)
print(y)

# 삭제 : del, remove, pop

# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)
print()
print()

z = (5, 2, 1, 3, 4)

print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용
print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 89 and score2 == 'A':
    print("합격하셨습니다.")
else:
    print("죄송합니다. 불합격입니다.")

# 다중조건문
num = 82

if num >= 90:
    print("num 등급 A" , num)
elif num >= 80:
    print("num 등급 B" , num)
elif num >= 70:
    print("num 등급 C" , num)
else:
    print("꽝")