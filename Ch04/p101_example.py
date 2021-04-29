"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 단어 빈도수 구하기 예시
"""

# 단어 데이터 셋
charset = ['abe', 'code', 'band', 'band', 'abc']
wc = {}  # 빈 셋

# get 함수 이용 : key 이용 해서 value 가져오기

for key in charset:
    wc[key] = wc.get(key, 0) + 1
    print(wc)
