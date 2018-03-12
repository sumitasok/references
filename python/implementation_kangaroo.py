# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/kangaroo/problem


def kangaroo(x1, v1, x2, v2):
    if v2 > v1:
        return 'NO'
    if x1 == x2:
        return 'YES'
    return step(x1, v1, x2, v2, 700)


def step(x1, v1, x2, v2, n):
    x1 = x1 + v1
    x2 = x2 + v2
    if x1 == x2:
        return 'YES'
    if n == 0:
        return 'NO'
    return step(x1, v1, x2, v2, n - 1)


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
