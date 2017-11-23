# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/plus-minus/problem
from read_write import readInt, readIntArray


def plusMinus(arr):
    plus, minus, zero = 0, 0, 0
    arrCount = len(arr)
    for i in arr:
        plus += 1 if i > 0 else 0
        minus += 1 if i < 0 else 0
        zero += 1 if i == 0 else 0
    return [plus / arrCount, minus / arrCount, zero / arrCount]


n = readInt()
arr = readIntArray()
for i in plusMinus(arr):
    print('%.5f' % i)
