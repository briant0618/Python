"""
날짜 : 2021/04/28
이름 : 김동현
내용 : Python 고급 함수 실습하기 p.129

"""


# default 매개변수
def hello(name='세준', age=21):  # hello 함수에 호출을 유연하게 하기위해 default 값인 21세와 세준이라는 매개변수 설정
    print('이름 : ', name)
    print('나이 : ', age)


hello()
hello('김유신')
hello('김춘추', 31)


# 가변 매개변수
def total(*nums):  # 매개변수 앞에 *를 선언한 매개변수 / *는 리스트다. / java 에서는 ...을 쓴다.
    tot = 0
    for n in nums:
        tot += n

    return tot


r1 = total(1)
r2 = total(1, 2)
r3 = total(1, 2, 3)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)


# 하나 이상의 return 값
def sum_and_multi(num1, num2):
    y1 = num1 + num2
    y2 = num1 * num2

    return y1, y2


rs1, rs2 = sum_and_multi(1, 2)
rs3, rs4 = sum_and_multi(3, 4)
print('rs1 : %d, rs2 : %d ' % (rs1, rs2))
print('rs3 : %d, rs4 : %d ' % (rs3, rs4))


# 변수에 저장하는 함수
def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


var1 = plus
var2 = minus

res1 = var1(1, 2)
res2 = var2(2, 3)

print('res1 : ', res1)
print('res2 : ', res2)

# 응용

cals = [plus, minus]

res3 = cals[0](3, 4)
res4 = cals[1](4, 6)

print('res3 : ', res3)
print('res4 : ', res4)

# 람다 함수( 익명 함수)

lam_plus = lambda x, y: x + y  # lambda 매개변수 : 리턴값 /  얘도 앞에 변수있어야대

result = lam_plus(2, 3)
print('result : ', result)
