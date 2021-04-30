from Ch06.sub1.Account import Account  # 출처 안써주면 에러뜹니당.


class StockAccount(Account):
    # Account 활용해서 상속받아서 재활용한다.
    def __init__(self, bank, id, name, money, stock, amount, price):
        self.stock = stock
        self.amount = amount
        self.price = price

        super().__init__(bank, id, name, money)

    def sell(self, amount, price):
        print('{}를 {}개 {}가격에 판매함'.format(self.stock, amount, price))

    def buy(self, amount, price):
        print('{}를 {}개 {}가격에 구매함'.format(self.stock, amount, price))

    def show(self):
        super().show()
        print('주식 종목 : ', self.stock)
        print('주식 종목 : ', self.amount)
        print('주식 종목 : ', self.price)
