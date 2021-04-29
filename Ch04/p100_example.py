"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 요소 검사 /  반복 예시
"""

# p99 요소 들고오기
dick = dict(key1=100, key2=200, key3=300)
print(dick)

person = {'name': '홍길동', 'age': '25', 'address': '서울시'}
print(person)
print(person['name'])
print(type(dick), type(person))

person['age'] = 45
print(person)

del person['address']
print(person)

person['pay'] = 250
print(person)


# 요소 검사

print(person['age'])
print('age' in person)

# 요소 반복하기

for key in person.keys():
    print(key)     # key 넘김
for v in person.values():
    print(v)       # value 넘김
for i in person.items():
    print(i)    # key / value 넘김

