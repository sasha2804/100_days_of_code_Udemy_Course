from tkinter import *
window = Tk()
window.title('Tkinter study')
window.minsize(600,400)

my_label = Label(text='The first label', font=('Arial', 24, 'bold'))
# my_label.pack(side='bottom', expand=True)
my_label.pack()

my_label['text'] = 'New Text'
my_label.config(text='New text')



input = Entry(width=10)
print(input.get())

# button
def button_clicked():
    print('Button clicked')
    # my_label['text'] = 'Button got clicked'
    # my_label.config(text='Button got clicked')
    my_label.config(text = input.get())


button = Button(text='Click me', command = button_clicked)
button.pack()


# entry component
input.pack()



window.mainloop()

