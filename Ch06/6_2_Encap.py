"""
날짜 : 2021/04/29
이름 : 김동현
내용 : python 객체지향 프로그래밍 캡슐화 p.161
"""

from Ch06.sub1.Account import Account

kb = Account('국민은행', '101-11-1091', '김유신', 30000)
kb.deposit(10000)
kb.withdraw(5000)

# kb.money -= 1   # 취약 코드 = 해킹시도. -> Account 이제.. 캡슐화되어 이제 에러가 뜹니당.
kb.show()
