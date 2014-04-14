#! /usr/bin/env python
# coding: utf-8


import itertools


def call_combinations(l):
    length = len(l)
    for i in range(length + 1):
        for c in itertools.combinations(l, i):
            print c


def call_permutations(l):
    length = len(l)
    for i in range(length + 1):
        for p in itertools.permutations(l, i):
            if sorted(p) == list(p):
                print p


def combination(l):
    pass

if __name__ == '__main__':
    l = raw_input()
    l = l.split()
    call_permutations(l)
