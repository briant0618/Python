"""
날짜 : 2021/04/28
이름 : 김동현
내용 : while 반복문 형식 예시
"""

# (1) count 와 누적 변수

cnt = tot = 0  # 변수를 초기화
while cnt < 5:   # True : loop 수행
    cnt += 1     # count 변수( cnt = cnt + 1)
    tot += cnt   # 누적 변수 ( tot = tot + cnt)
    print(cnt, tot)

# 실습해보자 / 1~100 사이의 3의 배수의 합과 원소 추출
cnt = tot = 0
dataset = []    # 빈 list

while cnt < 100:
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt   # 누적 변수
        dataset.append(cnt)   # cnt 추가
print(' 1 ~ 100 사이의 3의 배수의 합 = %d' % tot)
print('dataset = ', dataset)
