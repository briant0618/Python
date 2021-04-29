"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 튜플 관련 함수 예시
"""

# 튜플 자료형 변환하기

lst = list(range(1, 6))
t3 = tuple(lst)
print(t3)

# 튜플 관련 함수
print(len(t3), type(t3))
print(t3.count(3))
print(t3.index(4))
