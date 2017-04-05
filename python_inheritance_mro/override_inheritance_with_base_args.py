# -------------------------------------------------------
# --- Overriding with arguments in base constructor only
# -------------------------------------------------------

class A_ArgBase(object):
    def __init__(self,a=None):
        print("a_ArgBase"+str(a))


class B_ArgBase(A_ArgBase):
    def __init__(self):
        print("b_ArgBase")
        super(B_ArgBase, self).__init__()


class C_ArgBase(A_ArgBase):
    def __init__(self):
        print("c_ArgBase")
        super(C_ArgBase, self).__init__("C")


if __name__ == "__main__":
    A_ArgBase("a")
    B_ArgBase()
    C_ArgBase()
    
