import sys
from ..dir_A.caller_callee import my_callee


def callee():
    print(__file__ +" -> "+sys._getframe().f_code.co_name+"()")
    my_callee()
