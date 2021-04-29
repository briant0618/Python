"""
날짜 : 2021/04/28
이름 : 김동현
내용 : random 관련 함수 형식 2 예시
"""

# (1) random module 관련 함수 도움말
import random

help(random.randint)
help(random.choices)

# (2) 이름 list 에 전체이름/특정이름 출력

names = {'홍길동', '이승만', '심영', '김두한', '정진영'}
print(names)  # 전체 이름 출력

# (3) list 의 자료 유뮤 확인
if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 읎음')

# (4) 난수 정수로 이름 선택하기
idx = random.randint(0, 2)
print(names[idx])
