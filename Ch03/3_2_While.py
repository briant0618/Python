"""
날짜 : 2021/04/28
이름 : 김동현
내용 : Python 반복문 while 실습 p.64
"""

# while Basic Logic
num1 = 1

while num1 < 5:  # 조건이 참일떄 while 실행
    print('num1 : ', num1)
    num1 += 1  # 4번 반복해서 roof..

# 1부터 10까지의 합

k, sun = 1, 0

while k <= 10:
    sun += k
    k += 1
print('1부터 10까지의 합 : ', sun)

# 1부터 10까지 짝수의 합
i, tot = 1, 0

while i <= 10:

    if i % 2 == 0:
        tot += i

        i += 1
print('1부터 10까지 짝수의 합 : ', tot)

# break
num = 1

while True:  # 무한 루프로 만들겠다.
    if num % 5 == 0 and num % 7 == 0:
        break  # 특정조건에 일치되면 break 시켜버림. [ 반복문 탈출 ]

    num += 1
print('5와 7의 최소 공배수', num)

# continue

s, total = 1, 0

while s <= 10:
    s += 1

    if s % 2 == 1:  # 짝수일때만 밑의 total 로 내려간다.
        continue   # 반복문의 상위로 이동 하게 해쥼

    total += s
print('1부터 10까지의 짝수합 :', total)