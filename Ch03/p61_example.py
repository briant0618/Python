"""
날짜 : 2021/04/28
이름 : 김동현
내용 : 단일 조건문 형식 예시
"""

var = 10  # if 블럭에서 사용되는 변수
if var >= 5:
    print('var = ', var)
    print('var 는 5보다 크다')
    print('조건이 참일 경우에 실행')

print('항상 실행')

# 100 ~ 85는 우수 / 84 ~ 70는 저조 / 69이하는 사람아님

score = int(input('점수 등록 : '))

if 85 <= score <= 100:
    print('우수')
else:
    if score >= 70:
        print('저조')


