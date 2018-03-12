# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/apple-and-orange/problem


def inrange(s, t, d):
    if s <= d <= t:
        return True
    return False


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_range = [inrange(s, t, d + a) for d in apple]
orange_range = [inrange(s, t, d + b) for d in orange]

print(apple_range.count(True))
print(orange_range.count(True))
