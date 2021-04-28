"""
날짜 : 2021/04/28
이름 : 김동현
내용 : Python 기본 함수 실습하기 p.114

"""


# 함수 정의

def f(x):  # python 에서는 function 대신 def = define 을 쓴다.
    y = 2 * x + 3
    return y


# 함수 호출[실행]

r1 = f(1)  # r1이라는 변수로 함수를 호출하게 한다.
r2 = f(2)
r3 = f(3)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)


# 함수의 유형 1 - 둘다 있음 [ 가장 일반적인 유형 ]

def type1(x, y):
    z = x + y
    return z


rs1 = type1(1, 2)  # type1(인자값, 인자값)
rs2 = type1(2, 3)
print('rs1 :', rs1)
print('rs2 :', rs2)


# 함수의 유형 2 - 리턴값이 없음
def type2(items):
    total = 0
    for item in items:
        total += item
    print('items 합 : ', total)


type2([1, 2, 3, 4, 5])  # List
type2((2, 4, 6, 8, 10))  # Tuple


# 함수의 유형 3 - 매개변수가 없음
def type3():
    total = 0

    for i in range(11):
        total += i

    return total


result = type3()
print('result : ', result)


# 함수의 유형 4 - 둘다 없음
def type4():
    print('type4 result : ', type3())


type4()


# 확인 문제

def ggd(num):
    print(num, '단')
    for i in range(1, 10):
        print('{} * {} = {} '.format(num, i, num * i))


ggd(2)
ggd(5)
ggd(7)
