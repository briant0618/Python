"""
날짜:2021/04/27
이름 : 김동현
팁 : IO = Input OutPut
내용 :  Python 표준 입출력 실습 교재 p.42
"""
# Python 표준 출력
print('Hello', end='!')  # 표준 출력방법
print('Python')

print('010', '1234', '1111', sep='-')  # 많이 보면서 실력 늘려야합니당!


# Python 표준 입력

num = input('숫자 입력:')

print('입력한 숫자:', num)
print('num type:', type(num))  # 결과가 String 으로 뜨는데 '숫자' 이기 때문에 문자열로 인식함

# 입력받은 문자열을 숫자로 변환
result = int(num)
print('result :', result)
print('result type:', type(result))

# 서식 문자 출력
print('%d년 %d월 %d일 %s요일' % (2021, 4, 27, '화'))  # d = 데시멀 s = string 으로 각각 대입하러감

# 포맷 문자 출력
print('이름 : {}, 나이 : {}, 주소 : {}' .format('김유신', 23, '김해시'))
