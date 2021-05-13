"""
날짜 : 2021/05/13
이름 : 김동현
내용 : 쪽지 시험 10번 [ 가위/바위/보 게임 ]
"""

import random


def game():
    words = ['가위', '바위', '보']
    while True:
        you_word = input('가위, 바위, 보 입력하세요 : ')
        try:
            if you_word not in words:
                raise ValueError
        except ValueError:
            print('잘못 입력 하셨습니다.')
            continue
        else:
            break

    com_word = random.choice(words)

    print('컴퓨터 결과 : ', com_word)

    if com_word == '가위' and you_word == '가위':
        print('무승부!')
    elif com_word == '가위' and you_word == '바위':
        print('너의 승리!')
    elif com_word == '가위' and you_word == '보':
        print('너의 패배!')
    elif com_word == '바위' and you_word == '가위':
        print('너의 패배!')
    elif com_word == '바위' and you_word == '바위':
        print('무승부!')
    elif com_word == '바위' and you_word == '보':
        print('너의 승리!')
    elif com_word == '보' and you_word == '가위':
        print('너의 승리!')
    elif com_word == '보' and you_word == '바위':
        print('너의 패배!')
    elif com_word == '보' and you_word == '보':
        print('무승부!')


while True:
    game()
    print('0 : 종료, 1: 한번 더하기')
    again = int(input('입력 : '))

    if again == 0:
        break

print(' Game Over ')
