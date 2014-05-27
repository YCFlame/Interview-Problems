#! /usr/bin/env python
# coding: utf-8


class AutoIncrementList(list):

    def __init__(self, iterable):
        iterable = [v + 1 for v in iterable]
        super(AutoIncrementList, self).__init__(iterable)

    def __setitem__(self, key, value):
        '''
        slice 的 step 不为 1 的时候会对每个值走这个函数，
        此时要求 slice 与 value_li 的长度相等
        '''
        if isinstance(value, list):
            value = [v + 1 for v in value]
        else:
            value += 1
        super(AutoIncrementList, self).__setitem__(key, value)

    def __setslice__(self, start, stop, value_li):
        value_li = [value + 1 for value in value_li]
        super(AutoIncrementList, self).__setslice__(start, stop, value_li)

    def append(self, value):
        super(AutoIncrementList, self).append(value + 1)

    def insert(self, index, value):
        super(AutoIncrementList, self).insert(index, value + 1)


if __name__ == '__main__':
    x = AutoIncrementList((1, 2, 3, 4, 5))
    print x
    x[0:5:1] = [8, 9, 10]
    print x
