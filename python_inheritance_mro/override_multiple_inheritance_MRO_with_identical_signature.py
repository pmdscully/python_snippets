
# ------------------------------------------------
# --- - Overriding multiple inheritance with 
#       "method resolution order" (MRO) kword arguments 
#       in the constructor.
#   More on MRO, see https://learnpythonthehardway.org/book/ex44.html
# ------------------------------------------------

class Base1_IdenticalInitSignature(object):
    def __init__(self,a=None):
        print("Base1"+str(a))

class Base2_IdenticalInitSignature(object):
    def __init__(self,a=None):
        print("Base2"+str(a))


class A_IdenticalInitSignature(Base1_IdenticalInitSignature,Base2_IdenticalInitSignature):
    def __init__(self,**kwargs):
        print("Child")
        super(A_IdenticalInitSignature, self).__init__(**kwargs)



if __name__ == "__main__":
    A_IdenticalInitSignature(a="a")
    # => Matches to first base class init.
    
