"""
날짜 : 2021/05/03
이름 : 김동현
내용 : python 외부 패키지 설치 [ 특수 파일 처리 ] p.239
"""

from openpyxl import Workbook  # 이제 python 으로 excel 가능

# Excel 파일 쓰기


# 엑셀파일 객체 생성
workbook = Workbook()

#  활성화된 Sheet 선택
sheet = workbook.active

# 데이터 입력
sheet['A1'] = '홍길동'
sheet.append([1, 2, 3])
sheet.append(['김유신', '김춘추', '장보고'])
sheet.cell(6, 2, '사과')    # 6행 2열 [ B6 에 사과 집어넣기 ]

# 엑셀 저장 + 닫기

workbook.save('C:/Users/김동현/Desktop/Sample.xlsx')
workbook.close()

print('Excel 작업완료..')