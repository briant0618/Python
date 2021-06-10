"""
날짜 : 2021/05/24
이름 : 김동현
내용 : Coding Test => 상하 좌우
"""

n = int(input())

x, y = 1, 1
plans = input().split()  # 이동경로
for plan in plans:
    if plan == "L":  # L이면
        if y == 1:
            continue
        else:
            y -= 1
    if plan == "R":  # R이면
        if y == n:
            continue
        else:
            y += 1
    if plan == "U":  # U이면
        if x == 1:
            continue
        else:
            x -= 1
    if plan == "D":  # D이면
        if x == n:
            continue
        else:
            x += 1

print(x, y)
