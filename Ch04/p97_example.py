"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 셋 객체 예시
"""

# 중복 불가능
s = {1, 3, 5, 3, 1}
print(len(s))
print(s)

# 요소 선택
for d in s:
    print(d, end=' ')

print()

# 집합 관련 함수

s2 = {3, 6}
print(s.union(s2))  # 합집합
print(s.difference(s2))  # 차집합
print(s.intersection(s2))  # 교집합

# 추가.삭제 함수
s3 = {1, 3, 4, 5}
print(s3)

s3.add(7)   # 원소 추가
print(s3)

s3.discard(3)  # 원소 삭제
print(s3)
