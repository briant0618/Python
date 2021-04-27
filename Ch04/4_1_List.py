"""
날짜 : 2021/04/27
이름 : 김동현
내용 : Python 자료구조 List 실습 p.84
"""

# List 생성
list1 = [1, 2, 3, 4, 5]  # list 는 배열이다. [ index 번호 0,1,2,3,4 ]

print('list1 type:', type(list1))
print('list1[0]:', list1[0])
print('list1[2]:', list1[2])
print('list1[3]:', list1[3])

list2 = [5, 3.14, True, 'Apple']   # 서로 다른 타입도 List 로 저장가능
print('list2 type:', type(list2))
print('list2[0]', list2[0])
print('list2[3]', list2[3])
print('list2[2]', list2[2])

list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 리스트안에 리스트 = 2차원 배열 [입체적으로 생각합시다]
print('list3 type:', type(list3))
print('list3[0][0]:', list3[0][0])
print('list3[1][1]:', list3[1][1])
print('list3[2][2]:', list3[2][2])

# List 덧셈
animal1 = ['사자', '호랑이', '코끼리']
animal2 = ['곰', '기린', '강아지']

result = animal1+animal2

print('result:', result)

# List 수정, 추가, 삭제 [ 동적 List 라서 추가, 삭제가 가능] -  Tuple = 추가 삭제가 되지않음

nums = [1, 2, 3, 4, 5]
print('nums:', nums)

nums[1] = 7  # 수정
print('nums:', nums)

nums[2:4] = [8, 9, 10]  # 추가 = [ 2,3 자리에 ] => 8.9.10이 들어옴
print('nums:', nums)

nums[3:5] = []  # 삭제 = [3,4 자리를 날림]
print('nums:', nums)
