"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 단일 list 객체 색인 예시
"""

x = list(range(1, 11))
print(x)
print(x[:5])
print(x[5:])
print('index 2씩 증가')
print(x[::2])  # 홀수 색인
print(x[1::2])  # 1부터 시작하는 짝수 색인
