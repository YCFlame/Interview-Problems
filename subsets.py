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
        for p in itertools.permutations(range(length), i):
            if sorted(p) == list(p):
                print tuple(l[j] for j in p)


def call_product(l):
    length = len(l)
    for i in range(length + 1):
        for p in itertools.product(range(length), repeat=i):
            if len(set(p)) == i and sorted(p) == list(p):
                print tuple(l[j] for j in p)


def combination(l):
    pass

if __name__ == '__main__':
    l = raw_input()
    l = l.split()
    call_product(l)
