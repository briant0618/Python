"""
날짜 : 2021/04/27
이름 : 김동현
내용 : format 과 양식문자 예시
"""

# (1) format () 함수 인수 : format(value, "format")
print("원주율 = ", format(3.14159, "8.3f"))
print("금액 = ", format(10000, "10d"))
print("금액 = ", format(125000, "3,d"))


# (2) 양식 문자 인수 : print("%양식문자" %(값)
name = "홍길동"
age = 15
price = 125.500
print("이름 : %s, 나이 : %d, data = %.2f" % (name, age, price))
