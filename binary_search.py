#! /usr/bin/env python
# coding: utf-8


def binary_search(data, target):
    length = len(data)
    if length == 0:
        return -1

    low = 0
    high = length - 1
    # 等号存在的原因是为了检查 target == data[high] 的情况
    while low <= high:
        mid = low + (high - low) / 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# 以下两种算法因为使用了半开半闭区间，所以判断条件是 low < high，因为 data[high] 已经检查过或者不存在
def first_match(data, target):
    length = len(data)
    if length == 0:
        return -1

    low = 0
    # 开区间是为了处理长度为 1 的数组
    high = length
    # 不加等号是为了避免在 low == high 且 data[mid] >= target 时陷入死循环
    while low < high:
        mid = low + (high - low) / 2
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid

    if low >= length or data[low] != target:
        # 发现返回值为负数则取反减一即为插入位置（以 0 为起始，
        # python 中 list 的 insert 方法是在指定位置之前插入），
        # 之所以要减一是为了保证此时返回负数，与在位置 0 找到时区分开
        return -low - 1
    else:
        return low


def last_match(data, target):
    length = len(data)
    if length == 0:
        return -1

    low = -1
    high = length - 1
    while low < high:
        # 避免产生非法值，如 low = -1, high = 1 - 1 = 0, 则 low + (high - low) / 2 = -1
        # 亦即 [low, high] 时取 mid 是 high
        mid = high - (high - low) / 2
        if data[mid] > target:
            high = mid - 1
        else:
            low = mid

    if high < 0 or data[high] != target:
        # 最终收敛在 low == high，因为 low 是开区间，所以需要 -1，然后为了再强制变成负数，再减一
        return -high - 2
    else:
        return high

if __name__ == '__main__':
    data = [1, 2, 3, 3, 3, 5, 7, 9]
    print first_match(data, 2)
