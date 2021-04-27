"""
날짜 : 2021/04/27
이름 : 김동현
내용 : Python 자료구조 Tuple p.92
"""

# Tuple = [고정 List] 생성

tuple1 = (1, 2, 3, 4, 5)  # Tuple 은 소괄호 ()를 쓴다. tuple = 추가/삭제 불가능
print('tuple1 type:', type(tuple1))
print('tuple1[0]:', tuple1[0])
print('tuple1[4]:', tuple1[4])

tuple2 = ('서울', '대전', '대구', '부산', '광주')
print('tuple2 type:', type(tuple2))
print('tuple2[0]: %s' % tuple2[0])
print('tuple2[4]: {}'.format(tuple2[4]))


# tuple 수정, 추가, 삭제 X

tuple3 = 1, 2, 3, 4, 5   # 변수 5개에 저장
print('tuple3 type:', type(tuple3))

# tuple3[1] = 8
# tuple3[4] = []  추가/삭제가 불가능
