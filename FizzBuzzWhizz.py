#! /usr/bin/env python
# coding: utf-8

import traceback


class FizzBuzzWhizz(object):

    def __init__(self, *args):
        assert len(args) == 3
        assert all(x.isdigit() for x in args)
        args = [int(x) for x in args]
        assert all(0 < x < 10 for x in args)
        self.fizz, self.buzz, self.whizz = args

    def output(self, i):
        if ((i % 10 == self.fizz) or
            (i / 10 == self.fizz) or
            (i / 100 == self.fizz)):
            return "Fizz"

        result = "%s%s%s" % (
            "Fizz" if i % self.fizz == 0 else "",
            "Buzz" if i % self.buzz == 0 else "",
            "Whizz" if i % self.whizz == 0 else "",
        )

        return result if result else i

if __name__ == '__main__':
    while True:
        input = raw_input("Please input three numbers seperated by a space: ")
        if not input:
            break

        try:
            fizz_buzz_whizz = FizzBuzzWhizz(*input.split())
        except AssertionError:
            print traceback.format_exc()
        else:
            for i in range(1, 101):
                print fizz_buzz_whizz.output(i)
