#! /usr/bin/env python
# coding: utf-8


def check(data):
    stack = []
    start = {"[", "(", "{"}
    end = {"]", ")", "}"}
    quotation = {"'", '"'}
    map = {")": "(", "]": "[", "}": "{", "'": "'", '"': '"'}
    in_quote = False
    for i in data:
        if i in quotation:
            if in_quote:
                length = len(stack)
                temp = stack[length - 1]
                if i == temp:
                    stack.pop()
                    in_quote = False
            else:
                stack.append(i)
                in_quote = True

        elif in_quote:
            continue
        elif i in start:
            stack.append(i)
        elif i in end:
            try:
                temp = stack.pop()
                if temp != map[i]:
                    return False
            except IndexError:
                return False

    if stack:
        return False
    else:
        return True

if __name__ == '__main__':
    data = "'{}'(\"}\"[])"
    print check(data)
