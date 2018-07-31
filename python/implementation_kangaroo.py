# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/kangaroo/problem


def kangaroo(x1, v1, x2, v2):
    if v2 > v1:
        return 'NO'
    if x1 == x2:
        return 'YES'
    return step(x1, v1, x2, v2, 700)


def step(x1, v1, x2, v2, n):
    x1 = x1 + v1
    x2 = x2 + v2
    if x1 == x2:
        return 'YES'
    if n == 0:
        return 'NO'
    return step(x1, v1, x2, v2, n - 1)


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)


a = []
b = []
for i, x in enumerate([1, 2, 3, 4]):
    if (i % 2 == 0):
        a.append(x)
    if (i % 2 != 0):
        b.append(x)


def split_alternatively(list):
    a, b = [], []
    for i, x in list[::2]:
        if (i % 2 == 0):
            a.append(x)
        if (i % 2 != 0):
            b.append(x)
    return a, b


import itertools


def solution(a, b):
    da_count = a / 2
    sa_count = a % 2
    db_count = b / 2
    sb_count = b % 2

    base = zip((['aa'] * int(da_count)) + (['a'] * int(sa_count)),
               (['bb'] * int(db_count)) + (['b'] * int(sb_count)))
    merged = list(itertools.chain(*base))
    partial_result = ''.join([str(x) for x in merged])

    remaining = a + b - len(partial_result)
    if remaining == 0:
        return partial_result
    else:
        if (da_count + sa_count) > (db_count + sb_count):
            return partial_result + ''.join([str(x) for x in (['a'] * remaining)])
        else:
            return ''.join([str(x) for x in (['b'] * remaining)]) + partial_result


def solution(T):
    uniq = list(set(T))
    if len(uniq) < (len(T) / 2):
        return len(T) / 2
    else:
        return len(uniq)


def solution(T):
    # write your code in Python 3.6
    # Sort the candies, so that same types are listed together.
    candies = sorted(T)
    first_list, second_list = split_alternatively(candies)
    first_uniq_list = list(set(first_list))
    second_uniq_list = list(set(second_list))
    if len(first_uniq_list) > len(second_uniq_list):
        marys_uniq = first_uniq_list
    else:
        marys_uniq = second_uniq_list

    return len(marys_uniq)

# split the list by alternative items, so that similar items are moved to separate lists.


def split_alternatively(list):
    a, b = [], []
    for i, x in enumerate(list):
        if (i % 2 == 0):
            a.append(x)
        if (i % 2 != 0):
            b.append(x)
    return a, b


import itertools


def solution(a, b):
    # if a - b  or b - a  > 3  ?
    # a , b , alternate
    # doble each item
    # list = []
    # if a > b
    #ac = a/2 + (a%2)
    # b , a, b ,a
    # for
    # else
    # bc = b/2 + (b%2)
    # double a items possible

    remaining = abs(b - a)
    if a < b:
        r = ['bb', 'a'] * remaining + ['b', 'a'] * (a - remaining)

    else:
        r = ['aa', 'bb'] * remaining + ['a', 'b'] * (b - remaining)

    return ''.join([str(x) for x in r])

    da_count = a / 2
    # single a items possible
    sa_count = a % 2
    # double b items possible
    db_count = b / 2
    # single b items possible
    sb_count = b % 2

    base = zip((['aa'] * int(da_count)) + (['a'] * int(sa_count)),
               (['bb'] * int(db_count)) + (['b'] * int(sb_count)))
    merged = list(itertools.chain(*base))
    partial_result = ''.join([str(x) for x in merged])

    remaining = a + b - len(partial_result)
    if remaining == 0:
        return partial_result

    if (da_count + sa_count) > (db_count + sb_count):
        return partial_result + ''.join([str(x) for x in (['a'] * remaining)])
    else:
        return ''.join([str(x) for x in (['b'] * remaining)]) + partial_result

# https://app.codility.com/c/feedback/9NZG6V-R9A


import itertools


def solution(A, B):
    if A == B:
        base = ['ab'] * a
        return ''.join([str(x) for x in base])

    remaining = abs(a - b)
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


print(solution(7, 3))
