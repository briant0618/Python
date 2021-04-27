"""
날짜 : 2021/04/27
이름 : 김동현
내용 : Python 조건문 if문 실습 p.68
"""

# If
num1, num2 = 1, 2

if num1 > 0:
    # 이 안은 if 문 Scope 이다.
    print('num1은 0보다 크다')

if num1 > num2:
    print('num1은 num2보다 크다')
    # 얘는 false 라서 출력 안됨

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다')
if num1 < 0 and num2 > 1:
    print('num1은 0보다 크고 num2는 1보다 크다')  # 위의 if 와 같은 문장이다.

# If Else

num3, num4 = 3, 4

if num3 > num4:
    print('num3이 num4보다 크다')   # 조건이 참일때
else:
    print('num3이 num4보다 작다')   # 조건이 거짓인 경우


# If ~ Elif ~ Else

if num1 > num2:
    print('num1이 num2보다 크다')
elif num2 > num3:
    print('num2이 num3보다 크다')
elif num3 > num4:
    print('num3이 num4보다 크다')
else:
    print('num4가 가장크다')


# 삼항 조건문

num = 5
result = num * 2 if num >= 5 else num + 2
# num*2 = 1항 / num >= = 2항 / num + 2 = 3항
# 항에 따라서 확인가능
print('result:', result)


# 연습문제
# score = input('점수 입력: ')
# score = int(score) ↓ 두개 통합하자.
score = int(input('점수 입력: '))
print('점수 확인: ', score)

if 90 <= score < 100:
    print('A 입니다.')
elif 80 <= score < 90:
    print('B 입니다.')
elif 70 <= score < 80:
    print('C 입니다.')
elif 60 <= score < 70:
    print('D 입니다.')
elif 60 > score:
    print('F 입니다.')
