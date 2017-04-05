
# ------------------------------------------------
# --- Overriding with kword arguments in constructor
# ------------------------------------------------

class A(object):
    def __init__(self,a=None):
        print("a"+str(a))


class B(A):
    def __init__(self,b, **kwargs):
        print("b"+str(b))
        super(B, self).__init__(**kwargs)



if __name__ == "__main__":
    A(a="a")
    B("a",a="b")
    
