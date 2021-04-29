"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 추가.삭제.수정.삽입 예시2
"""

# (1) 리스트 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]

z = x + y
print(z)

# (2) 리스트 확장

x.extend(y)
print(x)

# (3) 리스트 추가
x.append(y)
print(x)

# (4) 리스트 2배 확장
lst = [1, 2, 3, 4, 5, 6, 7]
result = lst * 2
print(result)
