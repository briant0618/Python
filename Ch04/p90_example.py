"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 리스트 정렬 + 요소검사 예시
"""

# ( 1) list 정렬

lst = [1, 2, 3, 4, 5, 6, 7]
result = lst * 2
print(result)

result.sort()  # 오름차순 정리
print(result)

result.sort(reverse=True)  # 내림차순 정리
print(result)

# (2) list 요소 검사
import random

r = []  # 빈 리스트
for i in range(5):
    r.append(random.randint(1, 5))

print(r)
if 4 in r:
    print('있음')
else:
    print('읎어요')
