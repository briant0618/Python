"""
날짜 : 2021/04/30
이름 : 김동현
내용 : 쪽지 시험 4번
"""

for i in range(1, 7):
    for j in range(1, 7):

        tot = (i + j)

        if tot == 6:
            print('첫번째 주사위 : %d, 두번째 수자위 : %d' % (i, j))
