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
sql = "UPDATE `User1` SET `hp`='010-1111-1111' "  # 두줄 만드려면 ' 과 " 사이에 한칸 띄워서 사용하자. 안그러면 그냥 위만 날라감.
sql += "WHERE `uid`='p101'; "
cur.execute(sql)
conn.commit()

# DB 종료
conn.close()

print('Update 완료..')