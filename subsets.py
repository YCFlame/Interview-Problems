#! /usr/bin/env python
# coding: utf-8


import itertools


def lasy_combination(l):
    length = len(l)
    for i in range(length + 1):
        for c in itertools.combinations(l, i):
            print c


def combination(l):
    pass

if __name__ == '__main__':
    l = raw_input()
    l = l.split()
    lasy_combination(l)
