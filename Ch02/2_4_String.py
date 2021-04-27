"""
날짜 : 2021/04/26
이름 : 김동현
내용 : Python String(문자열) 예제 p.48
"""

# 문자열 더하기
str1 = 'Hello'
str2 = 'Python'
str3 = str1 + str2
print('str3:', str3)

# 문자열 곱하기
name = '홍길동'
print('name * 3 :', name * 3)   # 이름 반복문이됨

# 문자열 길이

msg = 'Hello World'
print('msg 길이: ', len(msg))  # len= length[길이=문자갯수]

# 문자열 Index
print('msg 1번째 문자:', msg[0])
print('msg 7번째 문자:', msg[6])
print('msg -1번째 문자:', msg[-1])  # -1 은 0 앞으로 간다.

# 문자열 자르기
print('msg 0~5까지 문자열:', msg[0:5])
print('msg 처음~5까지 문자열:', msg[:5])
print('msg 5~마지막까지 문자열:', msg[5:])


# 문자열 분리
people = '김유신|강감찬|김춘추|강감찬|이순신'
p1, p2, p3, p4, p5 = people.split('|')
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

# 문자열 Escape
print('서울\n대전\n대구\n부산\n광주')  # 세로로
print('서울\t대전\t대구\t부산\t광주')  # tap = 한칸씩 띄워서.

print('저는 \'홍길동\' 입니다')
