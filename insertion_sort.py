#! /usr/bin/env python
# coding: utf-8

from binary_search import first_match


def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        index = first_match(array[:i], array[i])
        data = array.pop(i)
        if index < 0:
            index = -index - 1
        array.insert(index, data)

    return array

if __name__ == '__main__':
    array = [4, 6, 2, 3, 7, 9, 8, 3]
    print insertion_sort(array)
