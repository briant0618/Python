"""
날짜 : 2021/04/28
이름 : 김동현
내용 : Python 내장 함수  실습하기 p.118

"""

# 내장 함수

import math  # ceil 사용하기 위한 math 호출
import random  # 랜덤 모듈 쓰기위해 지정.
import time  # 타임 쓰기위해 지정.

# 수학 관련
r1 = abs(-5)  # abs = 절대값 ( +- 관계없이 그냥 +로 결과나옴 )
print('r1 : ', r1)

r2 = math.ceil(1.2)  # ceil = 올림함수 / 천장 함수라고도 한다.
r3 = math.ceil(1.8)

print('r2 : ', r3)
print('r2 : ', r3)

r4 = math.floor(1.3)  # floor = 내림함수 / 바닥 함수라고도 불린다.
r5 = math.floor(1.5)
print('r4 : ', r4)
print('r5 : ', r5)

r6 = round(1.5)  # round = 반올림 함수 / 내장함수라서 굳이~ 앞에 math 안붙여도댐.
print('r6 : ', r6)

# 제곱근

r8 = math.sqrt(7)  # sqrt = 루트 씌워버림.
r9 = math.sqrt(9)

print('r8 : ', r8)
print('r9 : ', r9)

# Random

num1 = random.random()
print('num1 : ', num1)  # random (0 ~ 1 사이에 임의의 실수 호출)

num2 = num1 * 20
print('num2 : ', num2)  # num1 * 20 = 0~20까지 임의 실수 호출

num3 = math.ceil(num2)
print('num3 : ', num3)  # 1 ~ 20 사이의 정수를 호출

num4 = math.ceil(random.random() * 20)
print('num4 : ', num4)  # 한줄로 압축한 코드 중첩본. [ num1 ~ num3의 치환된 것을 보고 중첩시킴]

# 날짜 / 시간

t1 = time.time()
print('t1 : ', t1)  # 출력하면 이상한 숫자뜸  [ 숫자 = unix time ]

t2 = time.ctime()
print('t2 : ', t2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
day = time.strftime('%d', now)
hour = time.strftime('%H', now)
mini = time.strftime('%m', now)
sec = time.strftime('%S', now)

print('%s년 %s월 %s일' % (year, month, day))
print('%s시 %s분 %s일' % (hour, mini, sec))

