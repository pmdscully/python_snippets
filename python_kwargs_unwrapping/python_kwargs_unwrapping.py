
def f(my=None, keywords=None):
    print(my)
    print(keywords)

def f_caller(new=None, **kwargs):
    print(new)
    f(**kwargs)


f_caller(new="a",my="b",keywords="c")

