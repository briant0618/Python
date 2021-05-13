"""
날짜 : 2021/05/13
이름 : 김동현
내용 : 큰 수의 법칙
"""

# n , m , k 를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())

# n개의 숫자를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

# print('n : %d, m : %d, k : %d' % (n, m, k))
# print('data : ', data)

data.sort(reverse=True) # sort = 가장작은 숫자 / reverse 써서 큰수로 바꿈
# 가장 큰 수
first = data[0]

# 2번째로 큰 수
second = data[1]

result = 0

# k = 0 이되는 경우때문에 보존하기위해 repeat 으로 k를 조정
repeat = k

# Grid 기법..
for i in range(m):
    if repeat > 0:
        result += first
        repeat -= 1
    else:
        result += second
        repeat = k

print(result)
