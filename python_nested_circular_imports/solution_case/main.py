import sys

from dir_nest.dir_A import caller_callee


def main():
    print(__file__ +" -> "+sys._getframe().f_code.co_name+"()")
    caller_callee.caller()

if __name__ == "__main__":
    main()