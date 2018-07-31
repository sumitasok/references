# -*- coding: utf-8 -*-
from read_write import readIntArray, printArraySep


def sort(arr):
    if len(arr) == 1:
        return arr
    print('len', len(arr))
    for x in range(len(arr) - 1):
        i, y = arr[x], arr[x + 1]
        print(i, y)
        if i > y:
            arr[x], arr[x + 1] = i, y
        else:
            arr[x], arr[x + 1] = y, i
        print(arr)

    return sort(arr[0:len(arr) - 1]) + [arr[len(arr) - 1]]


# printArraySep(sort(readIntArray()))

def sort_asc(arr):
    return sorted(arr)


printArraySep(sort_asc(readIntArray()))
