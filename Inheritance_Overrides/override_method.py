
class Base:
    def __init__(self):
        pass
    def a(self):
        print("super")
    def b(self):
        self.a()

class Sub(Base):
    def __init__(self):
        Base.__init__(self)
    def a(self):
        print("subclass")

if __name__ == "__main__":
    s = Sub()
    s.a()       # Prints "subclass"
    s.b()       # Prints "subclass"
    b = Base()
    b.a()       # Prints "super"
    b.b()       # Prints "super"
