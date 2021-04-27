"""
날짜 : 2021/04/27
이름 : 김동현
내용 : 자료형 변환 예시
"""

# 실수 -> 정수
a = int(10.5)
b = int(20.42)
add = a + b
print('add = ', add)

# 정수 -> 실수

a = float(10)
b = float(20)

add2 = a + b
print('add2 = ', add2)

# 논리형 -> 정수
print(int(True))  # 1이 된다.
print(int(False))  # 0이 된다.

# 문자형 -> 정수
st = '10'
print(int(st)**2)  # 제곱연산함
