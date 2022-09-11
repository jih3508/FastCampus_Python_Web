# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 후 생성 사용

# 선언
# class 클래스명:
#   함수
#   함수
#   함수

# 예제1
from unicodedata import name


class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1), id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 예제2
# self의 이해
class SelfTest():
    def function1():
        print('function1 called!')
    def function2(self): # 객체생성 해야 사용할수 있음
        print('function2 called!')

self_test = SelfTest()
# self_test.function1()
SelfTest.function1()
self_test.function2()

print(id(self_test))

# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0 # 모든 생성자에 공유가됨
    def __init__(self, name) :
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

# 자기 네임스페이스 없으면 class 네임스페이스에서 찾는다.
print(user1.stock_num) 
print(user2.stock_num)
print(user3.stock_num)

del user3 # 인스턴스 지우기