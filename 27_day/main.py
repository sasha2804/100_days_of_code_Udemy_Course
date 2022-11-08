import tkinter

window = tkinter.Tk()
window.title('Tkinter study')
window.minsize(600,400)

my_label = tkinter.Label(text='The first label', font=('Arial', 24, 'bold'))
my_label.pack(side='bottom', expand=True)




window.mainloop()

