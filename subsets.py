#! /usr/bin/env python
# coding: utf-8


import itertools


def call_combinations(l):
    length = len(l)
    for i in range(length + 1):
        for c in itertools.combinations(l, i):
            print c


def call_simple_combinations(l):
    for p in simple_combinations(l):
        print p


def simple_combinations(l):
    for p in simple_permutations(l):
        if sorted(p) == list(p):
            yield tuple(l[j] for j in p)


def simple_permutations(l):
    length = len(l)
    for i in range(length + 1):
        for p in itertools.product(range(length), repeat=i):
            if len(set(p)) == i:
                yield tuple(l[j] for j in p)


def combination(l):
    pass


if __name__ == '__main__':
    l = raw_input()
    l = l.split()
    call_simple_combinations(l)
