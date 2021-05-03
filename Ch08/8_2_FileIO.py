"""
날짜 : 2021/05/03
이름 : 김동현
내용 : python file Input/Output p.217
"""

# 파일 읽기 [ input ]

file1 = open('C:/Users/김동현/Desktop/Sample.txt', 'r')
# open(파일 속성안의 경로) [ python 에서 경로는 중간은 /를 써줘야한다.!] # r = read 모드로 연다.

line = file1.readline()

print('line : ', line)  # 얘들만 쓰면 1줄만 출력됨..

file1.close()  # 사람도 열면 닫으니까.. 얘도 열면 닫아야지..[ 논리적인 절차가 매우 중요하다.]

# 여러줄을 출력하기.

file2 = open('C:/Users/김동현/Desktop/Sample.txt', 'r')

while True:
    line = file2.read()

    if not line:
        break
    print(line)  # if not break 없으면 while True 는 내용없어도 무한반복해서 쭉쭉내려간다...

file2.close()

# 파일 쓰기 [ output ]

file3 = open('C:/Users/김동현/Desktop/Test.txt', 'w')  # 가상 경로를 만들었따리~ # W = write 모드로 열기.
file3.write("안녕하세요.\n")
file3.write("감사합니다.\n")
file3.write("안감사합니다.\n")
file3.write("반갑습니다.\n")
file3.write("안반갑습니다.\n")
file3.close()

# 예제 [ 구구단 output ]
file4 = open('C:/Users/김동현/Desktop/gugu.txt', 'w')
for a in range(2, 10):
    file4.write('%d단\n' % a)
    for b in range(1, 10):
        c = a * b
        file4.write('{} X {} = {}\n'.format(a, b, c))

file4.close()
