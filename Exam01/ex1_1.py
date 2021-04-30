"""
날짜 : 2021/04/30
이름 : 김동현
내용 : 쪽지 시험 1번
"""

name = input("이름을 입력하세요 : ")
age = input("나이를 입력하세요 : ")

year = 2021 - int(age)

print(name + '님은 ' + age + '세이고, ' + str(year) + ' 년도에 태어났습니다.')

# 평균 계산 출력
n1 = int(input("첫번째 숫자 : "))
n2 = int(input("두번째 숫자 : "))
n3 = int(input("세번째 숫자 : "))
mean = (n1 + n2 + n3) / 3

print(n1, n2, n3, "의 평균은 ", mean, "입니다.")
