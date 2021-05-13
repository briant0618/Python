"""
날짜 : 2021/05/13
이름 : 김동현
내용 : 쪽지 시험 4번 [로또]
"""

import math
import random


def lotto():
    lotto_set = set()

    while True:
        num = math.ceil(random.random() * 45)
        lotto_set.add(num)

        if len(lotto_set) == 6:
            break

    return list(lotto_set)


if __name__ == '__main__':
    lotto_nums = lotto()

    lotto_nums.sort()

    print(lotto_nums)
