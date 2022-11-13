from msilib.schema import Font
from tkinter import *

FONT = ('Helvetica', 14)

def converter():
    label_km_middle.config(text=round(float(user_in.get())*1.609344, 4))


window = Tk()
window.title('Miles to km converter')
window.minsize(400,200)
window.config(padx=50, pady=50)

# Entries
user_in = Entry(bd=1,text='enter value', width=10, font=FONT)
user_in.grid(column=1, row=1)

#Labels
label_miles = Label(text='Miles', font=FONT)
label_miles.grid(column=2, row=1)
label_miles.config(padx=5,pady=5)

label_km_left = Label(text='is equal to', font=FONT)
label_km_left.grid(column=0, row=2)
label_km_left.config(padx=5,pady=5)

label_km_middle = Label(text=0,font=FONT)
label_km_middle.grid(column=1, row=2)
label_km_middle.config(padx=5,pady=5)

label_km_right = Label(text='Km', font=FONT)
label_km_right.grid(column=2, row=2)
label_km_right.config(padx=5,pady=5)

#Buttons
calc_button = Button(text='calculate', width=8, font=FONT, command=converter)
calc_button.grid(column=1, row=3)

window.mainloop()
