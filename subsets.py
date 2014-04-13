#! /usr/bin/env python
# coding: utf-8


import itertools

if __name__ == '__main__':
    l = raw_input()
    l = l.split()
    length = len(l)
    for i in range(1, length + 1):
        for c in itertools.combinations(l, i):
            print c
