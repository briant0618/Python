"""
날짜 : 2021/05/03
이름 : 김동현
내용 : python 예외처리 p.212
"""

# try ~ except

num1, num2 = 1, 0
r1 = r2 = r3 = r4 = 0

try:  # try = 예외가 발생할 가능성이 있는 코드영역
    r1 = num1 + num2
    r2 = num1 - num2
    r3 = num1 * num2
    r4 = num1 / num2  # 여기서 에러가 발생 [ 프로그래밍에서 0으로 나누는건 에러남.. ] -> 예외처리하기.
    # try 안에잇으니 이제 밖에서 r4를 참조못함.

except:  # except  =  예외 발생시 처리할 코드 영역

    print(' 예외 발생~! ')  # 단점으로 코드의 일관성을 해쳐서 그냥 r 자체를 try 로 묶어버림

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)
print('r4 : ', r4)

# try ~ except ~ finally

people = ['김유신', '김춘추', '장보고']

try:
    # 예외가 발생할 가능성 있는 코드 영역.
    for i in range(4):
        print(people[i])  # range 4에서 index = 3의 값이 없음.. -> 예외 처리가능.
except IndexError:
    # 예외 발생시 처리할 코드 영역 [ 구체적으로 IndexError 까지 첨부함 ]
    print('유효하지 않은 index 참조.')
finally:
    # 예외 발생 여부 관계없이 마지막에 실행되는 코드영역.
    print('예외 처리 완료함..')

# try ~ except ~ else

animal = ['코끼리', '사자', '호랑이', '기린']
result = None

while True:  # 한번이 아닌 여러번 선택시키게하기.

    try:
        # 예외가 발생할 가능성 있는 코드 영역.
        print('동물을 선택해봅시당.')
        print('1:코끼리, 2:사자, 3:호랑이, 4:기린, 0:종료 ')

        answer = int(input('선택 : '))  # 여기서부터 에러터질일이 너무 많음..

        if answer == 0:
            break
        elif answer < 0:
            raise Exception('음수는 불가능함니다.')   # 인위적으로 에러를 만들어서 except 로 강제 이동.[예외 일으키기 (던지기)] 자바에서는 Throw 쓴당.

        result = animal[answer - 1]   # 여기서 음수 [-1]을 쓰면 -2가되어 딴거 선택이 가능이해서 elif 써서 막아버림.

    except Exception as e:  # Exception as e = 에러 내용 집어내준다.
        # 예외 발생시 처리할 코드 영역
        print('에러 내용 : ', e)
        print('정확히 숫자 0~4 사이의 숫자 입력하세요.')
    else:
        # 예외가 발생하지 않았을때 실행되는 코드 영역.
        print('선택한 동물은 : ', result)

    print('프로그램 종료.....')
