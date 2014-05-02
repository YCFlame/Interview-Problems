#! /usr/bin/env python
# coding: utf-8


def selection_sort(array):
    length = len(array)
    if length < 2:
        return array

    for i in range(length):
        candidate = i
        for j in range(i + 1, length):
            if array[j] < array[candidate]:
                candidate = j
        if candidate != i:
            array[i], array[candidate] = array[candidate], array[i]

    return array


if __name__ == '__main__':
    array = [2, 3, 4, 1, 7, 6, 9, 8]
    print selection_sort(array)
