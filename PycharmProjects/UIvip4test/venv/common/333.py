# coding=utf-8

import sys


class Hello():

    def hello(self):
        a = sys._getframe().f_code.co_name
        b = self.__class__.__name__
        return a,b



if __name__ == "__main__":
    h = Hello()
    print(h.hello())