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
sql = "DELETE FROM `User1` WHERE `uid`='p101';"
cur.execute(sql)
conn.commit()

# DB 종료
conn.close()

print('Update 완료..')