#! /usr/bin/env python
# coding: utf-8


def binary_search(data, target):
    length = len(data)
    if length == 0:
        return -1

    low = 0
    high = length - 1
    while low <= high:
        mid = low + (high - low) / 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == '__main__':
    pass
