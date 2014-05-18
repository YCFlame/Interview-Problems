#! /usr/bin/env python
# coding: utf-8


def shell_sort(array, step_li):
    length = len(array)
    for step in step_li:
        for i in range(step):
            start = i
            while start + step < length:
                if array[start] > array[start + step]:
                    array[start], array[start + step] = array[start + step], array[start]

                start += step

    return array

if __name__ == '__main__':
    step_li = [4, 2, 1]
    array = [9, 7, 8, 6, 2, 1, 3, 5, 4]
    print shell_sort(array, step_li)
