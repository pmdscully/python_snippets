
# ------------------------------------------------
# --- Overriding with arguments in constructor
# ------------------------------------------------

class A(object):
    def __init__(self,a):
        print("a"+str(a))


class B(A):
    def __init__(self,b, *args): #**kwargs
        print("b"+str(b))
        super(B, self).__init__(*args) #**kwargs





if __name__ == "__main__":
    A("a")
    B("a","b")
    
