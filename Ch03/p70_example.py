"""
날짜 : 2021/04/28
이름 : 김동현
내용 : for 반복문 예시
"""

# (1) 문자열 열거행객체 이용

string = "심영"
print(len(string))    # 문자 길이 = 2
for s in string:
    print(s)

# (2) list 열거행객체 이용
listset = {1, 2, 3, 4, 5}

for e in listset:
    print('원소 : ',  e)
