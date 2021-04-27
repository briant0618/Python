"""
날짜 : 2021/04/27
이름 : 김동현
내용 : 대입 연산자 예시
"""

# (1) 변수에 값을 할당 (=)
i = tot = 10   # i=10; tot=10
i += 1  # i++ -> i = i+1
tot += i  # tot = tot+i
print(i, tot)

# 같은 줄에 중복으로 출력
print('출력1', end=',')   # end 는 구분자이다.
print('출력2')

# (2) 변수의 교체
v1, v2 = 100, 200
v2, v1 = v1, v2
print(v1, v2)  # 변수가 서로 바뀌게 됨

# (3)  packing 할당

lst = [1, 2, 3, 4, 5]
v1, *v2 = lst
print(v1, v2)

*v1, v2 = lst
print(v1, v2)

