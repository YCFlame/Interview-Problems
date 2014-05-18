#! /usr/bin/env python
# coding: utf-8


def merge_sort(array):
    length = len(array)
    start = 0
    step = 1
    temp = [0 for i in range(length)]
    while step < length:
        start = 0
        while start < length:
            current = i = start
            j = start + step
            while i < start + step and j < start + 2 * step and j < length:
                if array[i] <= array[j]:
                    temp[current] = array[i]
                    i += 1
                else:
                    temp[current] = array[j]
                    j += 1

                current += 1

            while i < start + step and i < length:
                temp[current] = array[i]
                i += 1
                current += 1

            while j < start + 2 * step and j < length:
                temp[current] = array[j]
                j += 1
                current += 1

            start += 2 * step

        step *= 2
        array, temp = temp, array

    return array

if __name__ == '__main__':
    array = [9, 2, 3, 4, 1, 6, 5, 7, 8]
    print merge_sort(array)
