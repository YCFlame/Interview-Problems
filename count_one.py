#! /usr/bin/env python
# coding: utf-8


def count_one(a):
    count = 0
    while a:
        a = a & (a - 1)
        count += 1
    print count

if __name__ == '__main__':
    count_one(13)
