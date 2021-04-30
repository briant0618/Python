
# Class Define [ like 설계도 만들기 ]
class Account:
    # class = 대문자로 시작해서 정의하는 것이 관례.
    # 속성과 기능으로 이루어져있다.
    # 속성 = 정보
    def __init__(self, bank, id, name, money):  # self 로 정의 된것들은 init 에서도 선언되야한다.
        self.__bank = bank  # 멤버 변수 선언 => self 를 통해 이 변수들이 account 의 멤버임을 표시
        self.__id = id
        self.__name = name
        self.__money = money

    #  _가 2개 나오는 것은 특수함수이다. / init = 실체 객체로 만들어 질때 생성하는 함수
    # self = 기능 x -> 그냥 매개변수가 멤버를 표시하는 것.

    # 기능
    def deposit(self, money):
        self.__money += money  # 입금하기.

    def withdraw(self, money):
        self.__money -= money  # 출금하기.

    def show(self):
        print('--------------------------')
        print('은행명 : ', self.__bank)
        print('계좌변호 : ', self.__id)
        print('입금주 : ', self.__name)
        print('잔액 : ', self.__money)  # 현실 계좌를 추상화하여 제작해서 딴곳으로 빼놧음.
