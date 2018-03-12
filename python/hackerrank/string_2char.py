# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/two-characters/problem

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
    return False


def isadj(s):
    if len(s) < 2:
        return s
    if s[0] == s[1]:
        b = isadj(s[2:])
        return '' + b
    a = isadj(s[1:])
    return s[0] + a


def findchars(s):
    return list(set(list(s)))


def length(s):
    s = super_reduced_string(s)
    chars = findchars(s)

    max_len = 0
    if len(chars) >= 2:
        for i, a in enumerate(chars[:len(chars) - 1]):
            for j, b in enumerate(chars[i + 1:]):
                stmp = s
                for x in chars:
                    if x != a and x != b:
                        stmp = stmp.replace(x, '')
                if hasadj(stmp) == False:
                    if max_len < len(stmp):
                        max_len = len(stmp)
        return max_len
    else:
        return len(s)


while(True):
    s_len = int(input().strip())
    s = input().strip()
    print(length(s))
