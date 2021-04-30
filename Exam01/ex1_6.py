"""
날짜 : 2021/04/30
이름 : 김동현
내용 : 쪽지 시험 6번
"""

count = 0

for i in range(1, 10):

    if i <= 5:
        count += 1
    else:
        count -= 1

    for j in range(5 - count):
        print(' ', end='')
    for k in range(count * 2 - 1):
        print('*', end='')

    print()
