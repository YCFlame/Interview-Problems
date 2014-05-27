#! /usr/bin/env python
# coding: utf-8


class LowerKey(dict):

    def __getitem__(self, key):
        key = key.lower()
        return super(LowerKey, self).__getitem__(key)

    def __setitem__(self, key, value):
        key = key.lower()
        super(LowerKey, self).__setitem__(key, value)

if __name__ == '__main__':
    x = LowerKey()
    x['YAng'] = "chao"
    print x
    print x['yAng']
