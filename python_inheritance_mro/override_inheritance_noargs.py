# ------------------------------------------------
# --- Overriding with no arguments in constructor
# ------------------------------------------------

class A_noArg(object):
    def __init__(self):
        print("a_noArg")


class B_noArg(A_noArg):
    def __init__(self):
        super(B_noArg, self).__init__()
        print("b_noArg")




if __name__ == "__main__":
    A_noArg()
    B_noArg()
