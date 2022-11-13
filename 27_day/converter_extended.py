from msilib.schema import Font
from tkinter import *
from tkinter.tix import COLUMN

FONT = ('Helvetica', 14)

# def converter():
#     label_km_middle.config(text=round(float(user_in.get())*1.609344, 4))


window = Tk()
window.title('Miles to km converter')
window.minsize(400,200)
window.config(padx=50, pady=50)

# Entries
# user_in = Entry(bd=1,text='enter value', width=10, font=FONT)
# user_in.grid(column=1, row=1)

#Listbox left
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

listbox_left = Listbox(height=3,exportselection=0, width=19)
distance_left = ["Mile", "Kilometer", "Meter"]
for item in distance_left:
    listbox_left.insert(distance_left.index(item), item)
# listbox_left.bind("<<ListboxSelect>>", listbox_used)
listbox_left.grid(column=0, row=0)



#Listbox right
listbox_right = Listbox(height=3,exportselection=0, width=19)
distance_right = distance_left.copy()
for item in distance_right:
    listbox_right.insert(distance_right.index(item), item)
# listbox_left.bind("<<ListboxSelect>>", listbox_used)
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


#Buttons
calc_button = Button(text='calculate', width=8, font=FONT)
calc_button.grid(column=0, row=2)




#Labels
# label_miles = Label(text='Miles', font=FONT)
# label_miles.grid(column=2, row=1)
# label_miles.config(padx=5,pady=5)

# label_km_left = Label(text='is equal to', font=FONT)
# label_km_left.grid(column=0, row=2)
# label_km_left.config(padx=5,pady=5)

# label_km_middle = Label(text=0,font=FONT)
# label_km_middle.grid(column=1, row=2)
# label_km_middle.config(padx=5,pady=5)

# label_km_right = Label(text='Km', font=FONT)
# label_km_right.grid(column=2, row=2)
# label_km_right.config(padx=5,pady=5)

#Buttons
# calc_button = Button(text='calculate', width=8, font=FONT, command=converter)
# calc_button.grid(column=1, row=3)


# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()





window.mainloop()
