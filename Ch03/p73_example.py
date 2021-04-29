"""
날짜 : 2021/04/28
이름 : 김동현
내용 : list 자료구조 예시
"""

# (1) list에 자료 저장하기
import random

lst = []  # 빈 list 만들기
for i in range(10):
    r = random.randint(1, 10)
    lst.append(r)
print('lst = ', lst)
