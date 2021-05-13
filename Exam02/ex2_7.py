"""
날짜 : 2021/05/13
이름 : 김동현
내용 : 쪽지 시험 7번
"""


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def hello(self):
        print('------------')
        print('이름 : ', self._name)
        print('나이 : ', self._age)


class student(Person):
    def __init__(self, name, age, school, major):
        super().__init__(name, age)
        self._school = school
        self._major = major

    def hello(self):
        super.hello()
        print('------------')
        print('이름 : ', self._school)
        print('나이 : ', self._major)


class salarystudent(Person):
    def __init__(self, name, age, school, major, company):
        super().__init__(name, age, school, major)
        self._company = company

    def hello(self):
        super.hello()
        print('------------')
        print('이름 : ', self._company)


if __name__ == '__main__':
    kim = Person('김유신')
    kim.hello()
    jang = Student('김유신')
    jang.hello()
    lee = Developer('장보고')
    lee.hello()
