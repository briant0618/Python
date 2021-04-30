"""
날짜 : 2021/04/29
이름 : 김동현
내용 : 패키지와 모듈 p.175
"""

# 패키지 = 모듈과 파일이 들어가는곳.
# from Ch06.sub2.StockAccount import StockAccount

# 가끔은 클래스가 아닌 패키지있음. = 모듈 파일.

import Ch06.sub2.calc        # 날 코딩 import (r1)
import Ch06.sub2.calc as c  # 그냥  import 하면 너무 번거로워서 c로 설정하기 위해 as 사용(r2)
from Ch06.sub2.calc import *  # 더 편한 설정..(r3/r4)

r1 = Ch06.sub2.calc.plus(1, 2)
r2 = c.minus(1, 3)
r3 = multi(3, 4)
r4 = div(4, 2)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)
print('r4 : ', r4)
