#! /usr/bin/env python
# coding: utf-8

from binary_search import first_match


def shell_sort(array, step_li):
    length = len(array)
    for step in step_li:
        for i in range(step):
            start = i
            temp = []
            while start < length:
                index = first_match(temp, array[start])
                if index < 0:
                    index = -index - 1
                temp.insert(index, array[start])
                start += step
            array[i::step] = temp

    return array

if __name__ == '__main__':
    step_li = [4, 2, 1]
    array = [9, 7, 8, 6, 2, 1, 3, 5, 4, 10, 0]
    print shell_sort(array, step_li)
