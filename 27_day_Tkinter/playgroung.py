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


# class Car():
#     def __init__(self, **kw):
#         self.make = kw.get('make')
#         self.model = kw.get('model')

# my_car = Car(make='Nissan', model='GT-R')
# print(my_car.model)

from tkinter import *

window = Tk()
window.title('Tkinter study')
window.minsize(600,400)


# Label #######
my_label = Label(text='The first label', font=('Arial', 24, 'bold'))
# my_label.pack()
my_label.grid(column = 0, row = 0)

my_label['text'] = 'New Text'
my_label.config(text='New text')

# Entry ########
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
# input.pack()

# Button 1 #######
def button_clicked():
    print('Button clicked')
    # my_label.config(text = input.get())
button_1 = Button(text='Click me', command = button_clicked)
# button.pack()
button_1.grid(column=1, row=2)

# Button 2 ########
button_2 = Button(text = 'New button', command = button_clicked)
button_2.grid(column = 2, row = 0)


window.mainloop()