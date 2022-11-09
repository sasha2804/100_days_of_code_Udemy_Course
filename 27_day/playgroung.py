
from ast import arg


def test_func(*args):
    print(sum(args))
    for i in args:
        print(i)
    


test_func(1,2,3,44,5)