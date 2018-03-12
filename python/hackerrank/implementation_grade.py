# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/grading/problem


def grade(i):
    if i < 38:
        return i
    if ((int(i / 5) * 5 + 5) - i) < 3:
        return int(i / 5) * 5 + 5
    return i


def solve(grades):
    return list(map(grade, grades))


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print('\n'.join(map(str, result)))
