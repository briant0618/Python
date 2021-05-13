"""
날짜 : 2021/05/13
이름 : 김동현
내용 : 쪽지 시험 8번
"""

from re import sub

texts_re1 = ['abc동해물과 1234백두산이 efgh마르고 5678닳도록9', '^하느님이 보우하사!@# 우리나라 만세*']

print('texts_re1 : ', texts_re1)

# 숫자 제거
texts_re2 = [sub('[0-9]', '', text) for text in texts_re1]
print('texts_re2 : ', texts_re2)

# 특문 제거
texts_re3 = [sub('[!@#$%^&*]', '', text) for text in texts_re2]

print('texts_re3 : ', texts_re3)

# 영문자 제거
texts_re4 = [sub('[a-z]A-Z', '', text) for text in texts_re3]

print('texts_re4 : ', texts_re4)
