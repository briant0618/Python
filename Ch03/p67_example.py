"""
날짜 : 2021/04/28
이름 : 김동현
내용 : random 관련 함수 형식 1 예시
"""

# (1) random module 추가하기

import random
help(random)


# (2) random module의 함수 도움말
help(random.random)


# (3) 0~1 사이의 난수 실수
r = random.random()
print('r=', r)      # r은 0.3940임

# [실습하기] 난수 0.01 미만이면 종료후 난수 개수 출력하기

cnt = 0
while True:
    r = random.random()
    print(random.random())
    if r < 0.01:
        break
    else:
        cnt += 1
print('난수 개수 = ', cnt)