# -*- coding: utf-8 -*-
from read_write import readIntArray, printArraySep


def ensure_non_zero(x):
    if x == 0:
        return 1
    return x


def solution(A):
    # write your code in Python 3.6
    a = sorted(A)

    for i, x in enumerate(a):
        if i == len(a) - 1:
            return ensure_non_zero(x + 1)
        if x <= 0:
            continue
        if x == a[i + 1]:
            continue
        xp = x + 1
        if xp != a[i + 1]:
            return ensure_non_zero(x + 1)
    return ensure_non_zero(a[-1] + 1)


print(solution(readIntArray()))
