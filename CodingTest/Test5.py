"""
날짜 : 2021/06/03
이름 : 김동현
내용 : Coding Test => 시각
"""

n = int(input())
count = 0

# ex] 

# hour = '170313'  <- 3이 2개 들어있지만 count는 1번한다!

# count = str(n) in hour  # 문자열로 바꿔서 진행.


for i in range(n+1):
    for j in range(60):
        for k in range(60):

                if '3' in str(i) + str (j) + str(k) :
                    count += 1


print(count)
