"""
날짜 : 2021/04/30
이름 : 김동현
내용 : 쪽지 시험 2번
"""

sum = 0

for k in range(1, 11):

    if k % 2 == 0 or k % 3 == 0:

      sum += k

print('2와 3의 배수의 정수의 합 :', sum)
