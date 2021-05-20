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
sql = "INSERT INTO `USER1` valus ('p101','김유신','010-1234-1001',25);"  # 로직은 같아서 sql 문만 바꾸면 됩니다.

cur.execute(sql)
conn.commit()

# DB 종료
conn.close()

print('Insert 완료..')

