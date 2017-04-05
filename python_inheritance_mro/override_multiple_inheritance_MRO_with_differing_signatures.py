
# ------------------------------------------------
# --- - Overriding multiple inheritance with 
#       "method resolution order" (MRO) kword arguments 
#       in the constructor.
#   More on MRO, see https://learnpythonthehardway.org/book/ex44.html
# ------------------------------------------------

class Base1_DifferingInitSignature(object):
    def __init__(self,a=None, *args, **kwargs):
        print("Base1"+str(a))

class Base2_DifferingInitSignature(object):
    def __init__(self,b=None, *args, **kwargs):
        print("Base2"+str(b))


class A_DifferingInitSignature(Base1_DifferingInitSignature, Base2_DifferingInitSignature):
    def __init__(self, *args, **kwargs):
        print("Child_A")
        super(A_DifferingInitSignature, self).__init__(*args,**kwargs)

class B_CallSecondBaseClassExplicitly(Base1_DifferingInitSignature, Base2_DifferingInitSignature):
    def __init__(self, *args, **kwargs):
        print("Child_B")
        Base2_DifferingInitSignature.__init__(*args,**kwargs)


if __name__ == "__main__":
    A_DifferingInitSignature(a="a")
    # => Matches to first base class init, because keyword matches.
    A_DifferingInitSignature(a="a",b="b")
    # => Matches to first base class init, because keyword matches. second base class init NOT run.
    A_DifferingInitSignature(b="b")
    # => Matches to first base class init, because **kwargs matches and 'a' defaults to None.
    A_DifferingInitSignature()
    # => Matches to first base class init, because 'a' defaults to None...
    B_CallSecondBaseClassExplicitly()

    
