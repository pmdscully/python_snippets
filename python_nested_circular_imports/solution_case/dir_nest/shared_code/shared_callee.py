import sys


def my_callee():
    print(__file__ + " -> " + sys._getframe().f_code.co_name + "()")