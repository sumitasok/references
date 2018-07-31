# -*- coding: utf-8 -*-
import itertools


def solution(a, b):
    if a == b:
        base = ['ab'] * a
        return ''.join([str(x) for x in base])

    remaining = abs(a - b) - 1
    base = []
    if a < b:
        pending = 'b'
        base = ['b', 'a'] * a + ['b']
    else:
        pending = 'a'
        base = ['a', 'b'] * b + ['a']

    itr = 1
    for i in range(remaining):
        base.insert((i * 2) + itr, pending)
        itr += 1

    return ''.join([str(x) for x in base])


print(solution(4, 1))
