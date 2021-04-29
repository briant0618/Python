"""
날짜 : 2021/04/28
이름 : 김동현
내용 : 중첩 조건문 형식 예시
"""

score = int(input('점수 입력: '))
grade = ''

if 85 <= score <= 100:
    grade = '우수'
elif score >= 70:
    grade = '보통'
else:
    grade = '사람이 아님'

print('당신의 점수는 %d이고, 등급은 %s' % (score, grade))
