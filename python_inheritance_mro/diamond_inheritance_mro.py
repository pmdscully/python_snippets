
"""
Method Resolution Order, for old (<2.2) and new (>=2.2) style classes.

Source: http://stackoverflow.com/a/1848647/1910555

OLD STYLE CLASSES: (2.x)
"""

class A: x = 'a'
class B(A): pass
class C(A): x = 'c'
class D(B, C): pass

print D.x
'a'


"""
Above, legacy-style (<=Py2.1), the method resolution order follows naive depth-first search.

As D - B - A - C - A 

This is the MRO algorithm.

So when looking up D.x, A is the first base in resolution 
order to solve it. Thereby hiding the definition in C
"""

"""
Below, new style classes (>=Py2.2). 
"""

class A(object): x = 'a'
class B(A): pass
class C(A): x = 'c'
class D(B, C): pass
print D.x
'c'

"""
Here, new-style, the order is:
"""
print D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)
    
"""
This is the C3-MRO algorithm:
- The gist is, search all derived classes before the base class. 
- It appears to be breadth-first, instead of depth-first search.
"""

