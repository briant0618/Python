"""
날짜 : 2021/04/29
이름 : 김동현
내용 : python 객체지향 프로그래밍 class p.148
"""
from Ch06.sub1.Account import Account  # Account 에서 Class 불러옴..
from Ch06.sub1.Computer import Computer

# 객체 생성 [ 인스턴스 만듦 => like 설계도면으로 제품 양산.] 객체는 큰틀에서는 변수이다.
kb = Account('국민은행', '101-102-10101', '김유신', 10000)  # Class 함수를 실행 -> init 실행이므로 init 의 멤버 변수에 대한 인자값 4개 넣어주세용.
kb.deposit(40000)  # 참조 연산자가 나옴. -> member 참조
kb.withdraw(7000)
kb.show()

wr = Account('우리은행', '101-102-33333', '김춘추', 30000)
wr.deposit(10000)
wr.withdraw(5000)
wr.show()

# Computer 객체 생성

Samsung = Computer('삼성', 'intel i7', '16GB', '1TB')
imac = Computer('애플', 'intel i7', '16GB', '1TB')
LG = Computer('엘지', 'intel i7', '16GB', '1TB')

Samsung.info()
imac.info()
LG.info()
