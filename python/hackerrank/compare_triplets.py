# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

from read_write import readIntArray, printArraySep


def compare_triplets(aS, bS):
    a, b = 0, 0
    for aV, bV in zip(aS, bS):
        a += 1 if aV > bV else 0
        b += 1 if aV < bV else 0
    return [a, b]


aS = readIntArray()
bS = readIntArray()
printArraySep(compare_triplets(aS, bS))
