#! /usr/bin/env python
# coding: utf-8


def unidirection_bubble_sort(array):
    length = len(array)
    for i in range(length):
        j = 1
        while j < length - i:
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            j += 1

    return array


def bidirection_bubble_sort(array):
    length = len(array)
    start, end = 0, length - 1
    while start < end:
        i = start
        while i < end:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            i += 1

        while i > start:
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

        start += 1
        end -= 1

    return array

if __name__ == '__main__':
    array = [9, 3, 2, 4, 6, 5, 7, 8, 1]
    print unidirection_bubble_sort(array)
    print bidirection_bubble_sort(array)
