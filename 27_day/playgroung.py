
from ast import arg
from gc import callbacks


# def test_func(*args):
#     print(sum(args))
#     for i in args:
#         print(i)
    


# test_func(1,2,3,44,5)


# def calc (n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     # print(kwargs['add'])

#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)


# calc(2, add=3, multiply=5)


class Car():
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make='Nissan', model='GT-R')
print(my_car.model)

