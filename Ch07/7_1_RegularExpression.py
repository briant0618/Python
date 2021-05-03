"""
날짜 : 2021/05/03
이름 : 김동현
내용 : python 정규 표현식 p192
"""

# 정규 표현식 ( regular expression)


from re import findall, match  # 정규 표현식 import

str1 = ' 1234 abc홍길동 ABC_555_6 부산광역시'

# 숫자 검색

print(findall('1234', str1))  # str1 속에서 1234라는 문자열을 찾기.
print(findall('[0-9]', str1))  # [ 0 - 9 ] = 전체 문자열 안에서 0에서 9까지의 숫자를 검색.
print(findall('[0-9]{3}', str1))  # [ 0 - 9 ]{3} = 전체 문자열 안에서 0에서 9까지의 숫자를 검색하는데 연속 3번 숫자 나오는놈 검색 . {}는 ()안에서는 반복문임.
print(findall('[0-9]{3,}', str1))  # [ 0 - 9 ]{3} = 전체 문자열 안에서 0에서 9까지의 숫자를 검색하는데 연속 3번이상 숫자 나오는놈 검색 .

# 문자열 검색
print(findall('[가-힣]{3,}', str1))  # 문자열에서 3자이상 한글을 찾자.
print(findall('[a-z|A-Z]{3,}', str1))  # 문자열에서 3자이상 영어문자를 찾자.[소문자 + 대문자]

str2 = 'test1abcABC 123mbc 45test'

print(findall('^test', str2))  # ^ = carrot [ 정규표현식에서 시작을 뜻함. -> test 로 시작되는놈 찾기 ]
print(findall('st$', str2))  # $ = [ 정규표현식에서 끝을 뜻함. -> st로 끝나는놈 찾기 ]

# 단어 검색

str3 = 'test^홍길동 abc 대한*민국 123$tbc'

print(findall('\\w{3,}', str3))  # 여기서 w는 word -> 3자 이상 단어 검색

# 응용하기

jumin = '123456-1812928'

result = match('[0,9]{6}-[1-2][0-9]{6}', jumin)  # 대쉬 - 의 앞에 0~9까지 6개의 숫자 뒤는 1~2의 숫자1개+ 0~9까지의 6개 숫자 있냐?

if result:
    print('주민 번호가 맞슴니다')
else:
    print('주민 번호가 아님니당')
