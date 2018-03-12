# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
from read_write import readInt, sort, readIntArray, printArraySep

n = readInt()
arr = sort(readIntArray())
print(arr.count(arr[0]))
