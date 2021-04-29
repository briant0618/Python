"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 딕트 객체 예시
"""

# dict 생성 1
dic = dict(key1=100, key2=200, key3=300)
print(dic)

# dict 생성 2

person = {'name': '홍길동', 'age': '25', 'address': '서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

# 원소 수정 삭제 추가

person['age'] = 45
print(person)   # 수정

del person['address']
print(person)   # 삭제

person['pay'] = 250
print(person)   # 추가


