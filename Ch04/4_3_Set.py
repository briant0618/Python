"""
날짜 : 2021/04/27
이름 : 김동현
내용 : Python 자료 구조 Set 실습하기 p.96
"""

# Set 생성

set1 = {1, 2, 3, 4, 5, 3}  # Set 은 대괄호
# set1 에는 중복이 안되므로 최종적으로 5개가 있다

print('set1 type:', type(set1))
print('set1:', set1)

set2 = set('Hello World')
print('set2 type:', type(set2))
print('set2:', set2)   # 스페이스바 띄우기도 문자취급을 합니다.

# 집합 출력 (List 변환)
list1 = list(set1)  # List 함수로 변환 -> but 집합[set]때문에 순서가 변환될수도 있다. 엄밀히 말하면 순서의 기준이 없다. 할때마다 다름..
print('list1:', list1)
print('list1[0]:', list1[0])
print('list1[3]:', list1[3])

list2 = list(set2)
print('list2:', list2)
print('list2[0]:', list2[0])
print('list2[3]:', list2[3])
