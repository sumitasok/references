# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/mini-max-sum/problem
from read_write import readIntArray, sort


def min_max(arr):
    print(sum(arr[-4:]), sum(arr[:4]))


arr = sort(readIntArray())
min_max(arr)
