#! /usr/bin/env python
# coding: utf-8


def tree():
    result = {}
    data = []
    while True:
        i = raw_input()
        if not i:
            break

        data.append(i)

    for line in data:
        temp = line.split()
        result[temp[0]] = temp[1:]

    final = [(data[0].split()[0], 0)]
    while final:
        temp = final.pop(0)
        if temp[0] in result:
            x = []
            for i in result[temp[0]]:
                x.append((i, temp[1] + 1))
            final = x + final

        print '\t' * temp[1] + temp[0]


if __name__ == '__main__':
    tree()
