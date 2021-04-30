"""
날짜 : 2021/04/29
이름 : 김동현
내용 : python 객체지향 프로그래밍 상속 개념 p.163
"""

from Ch06.sub2.StockAccount import StockAccount

kb = StockAccount('KB증권', '101-12-1010', '김유신', 10000, '삼성전자', 10, 80000)

kb.deposit(40000)
kb.withdraw(10000)
kb.buy(10, 80000)
kb.sell(10, 70000)
kb.show()
