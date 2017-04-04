import sys
from ..dir_B.callee import callee
from ..shared_code.shared_callee import my_callee

def caller():
    print(__file__ + " -> " + sys._getframe().f_code.co_name + "()")
    my_callee()
    callee()


# def my_callee():
#     print(__file__ + " -> " + sys._getframe().f_code.co_name + "()")
#     print("--- End ---")