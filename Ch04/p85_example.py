"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 단일 list 객체 예시
"""

# (1) 단일 list 예시

lst = [1, 2, 3, 4, 5]
print(lst)
print(type(lst))

for i in lst:
    print(lst[:i])  # i 전까지 ㄱㄱ
