#! /usr/bin/env python
# coding: utf-8


def count_inversion(filename):
    with open(filename, 'r') as f:
        array = [int(line.strip()) for line in f]
        length = len(array)
        result = 0
        step = 1
        temp = [0 for i in range(length)]
        while step < length:
            print step
            start = 0
            while start < length:
                current = i = start
                j = start + step
                while i < start + step and j < start + 2 * step and i < length and j < length:
                    if array[i] <= array[j]:
                        temp[current] = array[i]
                        i += 1
                    else:
                        temp[current] = array[j]
                        j += 1
                        result += start + step - i

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

            step += step
            array, temp = temp, array

        print 'result', result

if __name__ == '__main__':
    count_inversion("IntegerArray.txt")
