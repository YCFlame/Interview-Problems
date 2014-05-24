#! /usr/bin/env python
# coding: utf-8


def recursive_quick_sort(array, start, end):
    if start >= end:
        return
    i = j = start + 1
    pivot = array[start]
    while j <= end:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]

    recursive_quick_sort(array, start, i - 2)
    recursive_quick_sort(array, i, end)

    return array


def non_recursive_quick_sort(array):
    stack = [(0, len(array) - 1)]
    while len(stack):
        start, end = stack.pop()
        i = j = start + 1
        pivot = array[start]
        while j <= end:
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1

            j += 1

        array[start], array[i - 1] = array[i - 1], array[start]

        if start < i - 2:
            stack.append((start, i - 2))
        if i < end:
            stack.append((i, end))

    return array

if __name__ == '__main__':
    array = [9, 4, 5, 3, 6, 2, 3, 7, 8, 1]
    print recursive_quick_sort(array, 0, len(array) - 1)
    print non_recursive_quick_sort(array)
