"""
날짜 : 2021/05/20
이름 : 김동현
내용 : python DB SQL 실습
"""

import pymysql

# DB 접속
conn = pymysql.connect(host='192.168.10.114',
                       user='siopmy',
                       password='1234',
                       db='siopmy',
                       charset='utf8')
# SQL 실행 객체 생성
cur = conn.cursor()
# SQL 실행
sql = "SELECT * FROM `USER1`;"
cur.execute(sql)

# 결과 출력 [ select 는 result 를 DB 에서 받아야해서 추가해야함]
result_list = cur.fetchall()

for row in result_list:
    print('------------------------')
    print('아이디 : ', row[0])
    print('이름 : ', row[1])
    print('휴대폰 : ', row[2])
    print('나이 : ', row[3])
    print('------------------------')

# DB 종료
conn.close()

print('Select 완료..')