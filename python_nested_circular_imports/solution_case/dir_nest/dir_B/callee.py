import sys
from ..shared_code.shared_callee import my_callee


def callee():
    print(__file__ +" -> "+sys._getframe().f_code.co_name+"()")
    my_callee()
