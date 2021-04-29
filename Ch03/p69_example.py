"""
날짜 : 2021/04/28
이름 : 김동현
내용 : break / continue 예씨
"""

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 6:
        break
    print(i, end='')
    