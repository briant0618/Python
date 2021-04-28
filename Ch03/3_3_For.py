"""
날짜 : 2021/04/28
이름 : 김동현
내용 : Python 반복문 for 실습 p.70
"""

# for
for i in range(5):  # range 함수통해 for 가 반복된다.
    print('i : ', i)

for j in range(10, 20):
    print('j : ', j)
for k in range(10, 0, -1):  # range( start , end , 차감 )
    print('k : ', k)

# 1부터 10까지의 합
sum1 = 0
for k in range(11):
    sum1 += k
print('1부터 10까지의 합 : ', sum1)

# 1부터 10까지의 짝수 합
sum2 = 0

for k in range(11):
    if k % 2 == 0:
        sum2 += k
print('1부터 10까지의 짝수 합 : ', sum2)

# 중첩 for
for a in range(3):
    print('a : ', a)
    for b in range(4):
        print('b : ', b)     # 각 라운드마다 4번씩 총 3라운드 반복함

# 구구단
for x in range(2, 10):
    print(x, '단')
    for y in range(1, 10):
        z = x * y
        print('%d x %d = %d ' % (x, y, z))

# 별삼각형
for a in range(11):

    for b in range(a):

        print('☆', end='')

    print()

for c in range(10, 0, -1):

    for d in range(c):

        print('★', end='')
    print()

# Python 만 가능한 문법으로 별삼각형 만들기.
for i in range(10):
    print('○' * i)

# List 를 이용한 for -문
nums = [1, 2, 3, 4, 5]

for num in nums:   # range 대신 List 를 담은 nums 나옴
    print('num: ', num)

for person in ['김유신', '김춘추', '장보고']:
    print('person : ', person)

scores = [62, 86, 72, 74, 97]
total = 0

for score in scores:
    total += score

print('score 총합', total)

# List index , Value 출력

for index, value in enumerate(scores):
    print('{}, {}'.format(index, value))


# List Comprehension
list1 = [1, 2, 3, 4, 5]

list2 = [num*2 for num in list1]   # python 고유 문법 -> 알아 둡시다.
list3 = [num*3 for num in list1 if num % 2 == 1]  # num * 3 이지만 if -문으로 홀수만 찾음.

print('list2 : ', list2)
print('list3 : ', list3)
