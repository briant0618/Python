def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    return x / y


print('plus : ', plus(1, 2))
print('minus : ', minus(1, 2))   # 이게 package.py 에서도 실행이되버림..

if __name__ == '__main__':
    # 모듈 파일의 프로그램 시작점
    print('multi : ', multi(2, 3))
    print('div : ', div(2, 3))

    # 옆에 실행버튼이 나오고 실행이 가능하지만 목적은.. 시작점을 선언해서 의도치 않은 코드실행을 차단하는 것이다.
    # [ 위 print 는 package 에서 같이 실행 차단하기 위해서 만듦]
