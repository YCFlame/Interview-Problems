#! /usr/bin/env python
# coding: utf-8


def check(data, n):
    appear = set()
    start = end = 0
    result = ""
    next_start = start + 1
    while end < len(data):
        if data[end] not in appear:
            if len(appear) == n:
                if (end - start + 1) > len(result):
                    result = data[start:end]

                start = next_start
                next_start = start + 1
                appear = set(data[start:end])

            appear.add(data[end])
        else:
            # 如果遇到重复字符，下一次 start 跳转的时候就应该跳转到最后一个重复字符的地方，因为即使从中间开始也不会更长
            next_start = end

        end += 1
    return result


if __name__ == '__main__':
    data = "klsdjfowejlsjshdfjlsjf"
    print data
    print check(data, 4)
