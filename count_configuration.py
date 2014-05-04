#! /usr/bin/env python
# coding: utf-8

from itertools import combinations

"""
def count_configurations(a, b, c, n):
    count = 0
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i + j + k == n:
                    count += 1

    print count
"""


def count_configurations(a, b, c, n):
    ass = "a" * a
    bss = "b" * b
    css = "c" * c
    print len(set(combinations(ass + bss + css, n)))


"""
def count_configurations(a, b, c, n):
    count = 0
    for i in range(min(a, n) + 1):
        newn = n - i
        count += min(c, newn) - newn + min(newn, b) + 1
    print count
"""


if __name__ == '__main__':
    count_configurations(2, 3, 4, 6)
