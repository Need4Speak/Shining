# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/20 15:31
@Description : pass
"""
from functools import wraps


def single_dungeon_limit(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.flag:
            print 'aaaaaaaaaaa'
        else:
            return func(self, *args, **kwargs)

    return wrapper


class A(object):

    def __init__(self, flag):
        self.flag = flag

    @single_dungeon_limit
    def print_a(self):
        print 'a'

    @staticmethod
    def single_dungeon_limit(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.flag:
                print 'aaaaaaaaaaa'
            else:
                return func(self, *args, **kwargs)

        return wrapper


if __name__ == '__main__':
    a = A(True)
    a.print_a()
    a = A(False)
    a.print_a()
