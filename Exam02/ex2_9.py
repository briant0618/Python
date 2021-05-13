"""
날짜 : 2021/05/13
이름 : 김동현
내용 : 쪽지 시험 9번
"""

import math
import random

answer = math.ceil(random.random() * 45)
number = 0
count = 0

while True:
    count += 1
    print('-----------------')
    print('answer 맞춰보세요')
    number = input(' 1 ~ 45 사이의 값 입력 : ')

    try:
        # 문자를 숫자로 변환하기.
        number = int(number)

    except:
        print('숫자를 입력하심시오.')
        if answer == 0:
            continue

    if number < 0:
        print('음수는 입력할수 없습니다.')
        continue

    if answer > number:
        print('더 큰 숫자 입력하세요.')

    elif answer < number:
        print('더 작은 숫자 입력하세요.')

    else:
        print('정답 : ', answer)
        print('맞추셨습니다')
        print('시도 횟수 : %d회 ' % count)
        break
