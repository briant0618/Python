"""
날짜 : 2021/04/30
이름 : 김동현
내용 : 쪽지 시험 8번
"""

scores = [62, 82, 76, 88, 54, 92]

max = scores[0]
min = scores[0]

for score in scores:
    if max < score:
        max = score
    if min > score:
        min = score


print('최대값 : ', max)
print('최소값 : ', min)
