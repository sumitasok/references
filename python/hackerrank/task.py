# -*- coding: utf-8 -*-
def solution(N):
    # write your code in Python 3.6
    if N == 1:
        return [0]
    if N % 2 == 1:
        return list(range(-int(N / 2), 0)) + list(range(0, int(N / 2) + 1))
    if N % 2 == 0:
        return list(range(-int(N / 2), 0)) + list(range(1, int(N / 2) + 1))


# def solution(N):
#     # write your code in Python 3.6
#     str = "+-" * (N/2)
#     if (N%2) == 1:
#         str = str + "+"
#     return str
