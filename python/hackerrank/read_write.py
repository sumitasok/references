# -*- coding: utf-8 -*-
def solveMeFirst(a, b):
    # Hint: Type return a+b below
    return a + b


def readInt():
    return int(input())


def readIntArray(SEP=' '):
    return list(map(int, input().strip().split(SEP)))


def readStrArray(SEP=' '):
    return list(input().strip().split(SEP))


def readMxNmatrix(rowC, colC, MSEP=' ', NSEP=' '):
    mtx = []
    for x in range(0, rowC):
        mtx.append(readIntArray(MSEP))
    return mtx


def sort(arr):
    if len(arr) == 1:
        return arr

    for x in range(len(arr) - 1):
        i, y = arr[x], arr[x + 1]

        if i > y:
            arr[x], arr[x + 1] = i, y
        else:
            arr[x], arr[x + 1] = y, i

    return sort(arr[0:len(arr) - 1]) + [arr[len(arr) - 1]]


def printArraySep(arr, SEP=' '):
    print(SEP.join(map(str, arr)))

# print("input two numbers")
# num1 = readInt()
# num2 = readInt()
# res = solveMeFirst(num1,num2)
# print("output")
# print(res)

# print(readIntArray())
# print(readIntArray("-"))

# print(readStrArray())
