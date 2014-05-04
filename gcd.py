#! /usr/bin/env python
# coding: utf-8


def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if y == 0:
        return x
    if x & 1 == 0:
        if y & 1 == 0:
            return gcd(x >> 1, y >> 1) << 1
        else:
            return gcd(x >> 1, y)
    else:
        if y & 1 == 0:
            return gcd(x, y >> 1)
        else:
            return gcd(y, x - y)


if __name__ == '__main__':
    print gcd(16, 8)
