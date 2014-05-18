#! /usr/bin/env python
# coding: utf-8


def recursive_quick_sort(array, start, end):
    if start >= end:
        return
    i, j = start, end
    pivot = array[start]
    while i < j:
        # 一定要先移动 j，否则遇到最大的在第一个的时候就动不了了
        while i < j and array[j] >= pivot:
            j -= 1
        while i < j and array[i] <= pivot:
            i += 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    array[start], array[i] = array[i], array[start]

    recursive_quick_sort(array, start, i - 1)
    recursive_quick_sort(array, i + 1, end)

    return array

if __name__ == '__main__':
    array = [9, 4, 5, 3, 6, 2, 7, 8, 1]
    print recursive_quick_sort(array, 0, len(array) - 1)
