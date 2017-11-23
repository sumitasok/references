# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/staircase/problem
from read_write import readInt


def staircase(n):
    for x in range(n):
        print(' ' * (n - (x + 1)) + '#' * (x + 1))


staircase(readInt())
