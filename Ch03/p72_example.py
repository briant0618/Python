"""
날짜 : 2021/04/28
이름 : 김동현
내용 : range class 예시
"""

# (1) range 객체 생성

num1 = range(10)   # range(start)
print('num1 : ', num1)

num2 = range(1, 10)    # range( start , end)
print('num2 : ', num2)

num3 = range(1, 10, 2)  # range ( start , end , step)
print('num3 : ', num3)


# (2) range 객체 활용

for n in num1:
    print(n, end=' ')
print()
for n in num2:
    print(n, end=' ')
print()
for n in num3:
    print(n, end=' ')
print()
