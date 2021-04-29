"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 객체 주소 복사하기 예시
"""

# 얕은 복사 = 주소 복사
name = ['홍길동', '이순신', '강감찬']
print('name address = ', id(name))

name2 = name
print('name2 address = ', id(name2))

print(name)
print(name2)

# 원본 수정
name2[0] = "심영"
print(name2)
print(name)

# 깊은 복사 = 내용 복사
import copy

name3 = copy.deepcopy(name)
print(name)
print(name3)

print('name address = ', id(name))
print('name3 address = ', id(name3))
