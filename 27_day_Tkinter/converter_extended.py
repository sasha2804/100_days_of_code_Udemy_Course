from msilib.schema import Font
from tkinter import *
from tkinter.tix import COLUMN

FONT = ('Helvetica', 14)

def converter():
    entry_value = float(user_in.get())
    input_unit = listbox_left.get(listbox_left.curselection())
    output_unit = listbox_right.get(listbox_right.curselection())
    print(entry_value)
    print(input_unit)
    print(output_unit)
    if input_unit == 'Mile' and output_unit == 'Kilometer':
        label_out.config(text = entry_value*1.609344)
    elif input_unit == 'Kilometer' and output_unit == 'Mile':
        label_out.config(text = entry_value/1.609344)
    elif input_unit == 'Kilometer' and output_unit == 'Meter':
        label_out.config(text = entry_value*1000)
    elif input_unit == 'Meter' and output_unit == 'Kilometer':
        label_out.config(text = entry_value/1000)
    elif input_unit == 'Meter' and output_unit == 'Mile':
        label_out.config(text = entry_value/1000/1.609344)
    else:
        label_out.config(text = entry_value*1.609344*1000)

window = Tk()
window.title('Miles to km converter')
window.minsize(400,200)
window.config(padx=50, pady=50)


#Listbox left
listbox_left = Listbox(height=3,exportselection=0, width=19)
distance_left = ["Mile", "Kilometer", "Meter"]
for item in distance_left:
    listbox_left.insert(distance_left.index(item), item)
listbox_left.grid(column=0, row=0)

#Listbox right
listbox_right = Listbox(height=3,exportselection=0, width=19)
distance_right = distance_left.copy()
for item in distance_right:
    listbox_right.insert(distance_right.index(item), item)
listbox_right.grid(column=2, row=0)

#Label
label_miles = Label(text='>', font=FONT)
label_miles.grid(column=1, row=0)
label_miles.config(padx=5,pady=5)

label_in = Label(text='Enter value: ', font=FONT)
label_in.grid(column=0, row=1)
label_in.config(padx=5,pady=5)

label_res = Label(text='Result: ', font=FONT)
label_res.grid(column=0, row=3)
label_res.config(padx=5,pady=5)

label_out = Label(text=0, font=FONT)
label_out.grid(column=2, row=3)
label_out.config(padx=5,pady=5)

# Entries
user_in = Entry(bd=1, width=10, font=FONT)
user_in.grid(column=2, row=1)
entry_value = user_in.get()

#Buttons
calc_button = Button(text='calculate', width=8, font=FONT, command=converter)
calc_button.grid(column=0, row=2)



window.mainloop()
