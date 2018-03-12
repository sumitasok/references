# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/camelcase/problem

import sys


def strCount(s):
    count = 0
    if s == '':
        return 0
    if ord('A') <= ord(s[0]) <= ord('Z'):
        count = 1
    for c in s:
        if ord('A') <= ord(c) <= ord('Z'):
            count += 1
    return count


s = input().strip()
print(strCount(s))
