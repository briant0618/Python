"""
날짜 : 2021/04/28
이름 : 김동현
내용 : Python function Scope 실습하기 p.132

"""


def sum(x, y):
    tot = 0

    for k in range(x, y + 1):
        tot += k

    return tot


tot = 0  # 프로그램 시작
start = 1
end = 10


tot = sum(start, end)

print('tot : ', tot)
