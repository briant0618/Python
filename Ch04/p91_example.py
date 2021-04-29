"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 리스트 내포 예시
"""

# 형식1) 변수 = [ 실행문 for ]

x = [1, 3, 4, 6, 7]
# 이건 에러뜹니다 -> print(x ** 2)

lst = [i ** 2 for i in x]
print(lst)

# 형식2) 변수 = [ 실행문 for if ]  / 1 ~ 10 -> 2의 배수 추출 => i*2 -> list 저장

num = list(range(1, 15))
lst2 = [i * 2 for i in num if i % 2 == 0]
print(lst2)
