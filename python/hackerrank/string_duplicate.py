# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/reduced-string/problem
import sys


def super_reduced_string(s):
    stat = isadj(s)
    # empty
    if hasadj(stat):
        return super_reduced_string(stat)
    # no reducible - all single - an non adjacent
    return stat


def hasadj(s):
    for x in range(0, len(s) - 1):
        if s[x] == s[x + 1]:
            return True


def isadj(s):
    if len(s) < 2:
        return s
    if s[0] == s[1]:
        b = isadj(s[2:])
        return '' + b
    a = isadj(s[1:])
    return s[0] + a


s = input().strip()
result = super_reduced_string(s)
if result == '':
    print('Empty String')
else:
    print(result)
