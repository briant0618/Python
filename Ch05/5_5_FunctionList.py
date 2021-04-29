"""
날짜 : 2021/04/28
이름 : 김동현
내용 : Python List 함수  실습하기 p.88
"""

dataset = [1, 4, 3]  # list = python 에서 활용빈도가 제일 높음.
print('dataset : ', dataset)

# list 원소 추가(append)

dataset.append(2)
dataset.append(9)
print('2.dataset : ', dataset)  # 2개의 dataset 를 append[덧붙임] <- append = 는 자주쓰임

# list 정렬 (sort)
dataset.sort()
print('3.dataset : ', dataset)  # 오름 차순으로 정렬

dataset.sort(reverse=True)
print('4.dataset : ', dataset)  # 내림 차순

# list 원소(data) 삽입 (insert)

dataset.insert(2, 6)  # 2는 index -> index 2번과 3번 사이에 집어넣는다.
dataset.insert(1, 10)
print('5.dataset : ', dataset)

# list 삭제
dataset.remove(6)  # 해당 원소 6을 삭제.
print('6.dataset : ', dataset)


# map 함수 [코딩 테스트 할때 자주쓰임] - list 언소를 지정된 함수로 일괄 처리해줌.
# 여러 개의 데이터를 한번에 다른 형태로 변환할때 많이 사용.
def plus10(n):
    return n + 10


list1 = [1, 2, 3, 4, 5]
# list1_map = map(plus10, list1)    # map (함수이름, 매개변수)
# print('list1_map : ', list1_map)

list1_map_list = list(map(plus10, list1))  # 코드 중첩 함.
print('list1_map_list : ', list1_map_list)  # 위의 list object 분석하기 위해서 삽입.

list2 = [1.1, 2.2, 3.3, 4.4, 5.5]

# var1 = 1.12
# result = int(var1)  # int = 숫자의 실수부분을 날릴때도 쓰지만 문자열 string -> 숫자형 int 로 return 시켜서 숫자로 바꿔준다.
# print('result : ', result)

list2_map_list = list(map(int, list2))
print('list2_map_list : ', list2_map_list)

list3 = [1, 2, 3, 4, 5]
list3_map_list = list(map(lambda x: x * 2, list3))
print('list3_map_list : ', list3_map_list)

list4 = ['1', '2', '3', '4', '5']
list4_map_list = list(map(int, list4))
print('list4_map_list : ', list4_map_list)

# input 함수 확장하기 [ input = python 기본 입력 함수 ]
a = input('입력 : ')

print('a : ', a)

var1, var2, var3 = input('3개 숫자 입력(띄어쓰기 구분) : ').split()  # split 있어야 1개이상의 값을 동시에 받을 수 있다.

print('var1 : {}, var2 : {}, var3 : {} '.format(var1, var2, var3))
print('var1 + var2 + var3 = ', var1 + var2 + var3)  # 결과는 산술 연산이 아닌 문자열 합산이다.

# 숫자로 변환 -> map 함수 응용
num1, num2, num3 = map(int, input('3개 숫자 입력(띄어쓰기 구분) : ').split())
print('num1 : {}, num2 : {}, num3 : {} '.format(num1, num2, num3))
print('num1 + num2 + num3 = ', num1 + num2 + num3)
