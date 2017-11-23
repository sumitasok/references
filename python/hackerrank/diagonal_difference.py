# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/diagonal-difference/problem
from read_write import readInt, readMxNmatrix


def diagDiff(mtx):
    sumDiag = 0
    sumRevDiag = 0
    for x in range(0, len(mtx)):
        sumDiag += mtx[x][x]
    for x in range(0, len(mtx)):
        sumRevDiag += mtx[x][len(mtx) - 1 - x]
    return abs(sumDiag - sumRevDiag)


i = readInt()
mtx = readMxNmatrix(i, i)
print(diagDiff(mtx))
