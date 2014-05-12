#! /usr/bin/env python
# coding: utf-8


def check(data, n):
    appear = {}
    start = end = 0
    result = ""
    while end < len(data):
        if data[end] not in appear:
            if len(appear) == n:
                if (end - start + 1) > len(result):
                    result = data[start:end]

                while len(appear) == n:
                    appear[data[start]] -= 1
                    if appear[data[start]] == 0:
                        appear.pop(data[start])
                    start += 1

            appear[data[end]] = 1
        else:
            appear[data[end]] += 1

        end += 1

    return result


if __name__ == '__main__':
    data = "abbcabcdkjfelk"
    print data
    print check(data, 4)
