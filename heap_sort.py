#! /usr/bin/env python
# coding: utf-8

import operator


def heapify(array, pos, end, small=False):
    temp = array[pos]
    compare = operator.lt if small else operator.gt
    while 2 * pos + 1 <= end:
        child = 2 * pos + 1
        if child < end and compare(array[child + 1], array[child]):
            child += 1
        if compare(array[child], temp):
            array[pos] = array[child]
        else:
            break

        array[child] = temp
        pos = child


def heap_sort(array, reverse=False):
    length = len(array)
    for i in range(length / 2 - 1, -1, -1):
        heapify(array, i, length - 1, reverse)

    for i in range(length - 1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i - 1, reverse)

    return array

if __name__ == '__main__':
    array = [4, 2, 5, 6, 8, 1, 9, 0, 3]
    print heap_sort(array)
    print heap_sort(array, True)
