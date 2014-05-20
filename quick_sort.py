#! /usr/bin/env python
# coding: utf-8


def recursive_quick_sort(array, start, end):
    if start >= end:
        return
    i, j = start, end
    pivot = array[start]
    while i < j:
        # 一定要先移动 j，否则遇到最大的在第一个的时候 i 就会移动到末尾与 j 重合
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


def non_recursive_quick_sort(array):
    stack = [(0, len(array) - 1)]
    while len(stack):
        start, end = stack.pop()
        i, j = start, end
        pivot = array[start]
        while i < j:
            while i < j and array[j] >= pivot:
                j -= 1
            while i < j and array[i] <= pivot:
                i += 1
            if i < j:
                array[i], array[j] = array[j], array[i]

        array[start], array[i] = array[i], array[start]

        if start < i - 1:
            stack.append((start, i - 1))
        if i + 1 < end:
            stack.append((i + 1, end))

    return array

if __name__ == '__main__':
    array = [9, 4, 5, 3, 6, 2, 7, 8, 1]
    print recursive_quick_sort(array, 0, len(array) - 1)
    print non_recursive_quick_sort(array)
