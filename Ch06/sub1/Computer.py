def calc():
    print('Computer calc...')


class Computer:

    # 속성(특성)
    def __init__(self, brand, cpu, ram, hdd):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    # 기능
    def calculation(self):
        print('Computer calc.............')

    def info(self):
        print('-------------------------------------------------')
        print('컴퓨터 제조사 : ', self.brand)
        print('cpu 사양 : ', self.cpu)
        print('ram 사양 : ', self.ram)
        print('hdd 사양 : ', self.hdd)
