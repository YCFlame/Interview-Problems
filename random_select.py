#! /usr/bin/env python
# coding: utf-8


def random_select(array, n):
    start, end = 0, len(array) - 1
    while start != n - 1 and end != n - 1:
        pivot = array[start]
        i = j = start + 1
        while j <= end:
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1

            j += 1

        array[start], array[i - 1] = array[i - 1], array[start]

        if i - 1 < n - 1:
            start = i
        elif i - 1 > n:
            end = i - 2

    return array[n - 1]


if __name__ == '__main__':
    array = [2, 4, 1, 3, 6, 5, 8, 7, 9]
    print random_select(array, 6)
