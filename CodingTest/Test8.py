"""
날짜 : 2021/06/10
이름 : 김동현
내용 : python coding Test => 곱하기 or 더하기
"""

data = input()

result = int(data[0])  # 첫 번째 문자를 숫자로 변환해서 대입

for i in range(1, len(data)):

    num = int(data[i])

    # num 또는 result 가 0 혹은 1인 경우, 곱셈 연산 대신 덧셈 연산을 수행
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)