# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from random import randint
import tkinter
from tkinter import*
from tkinter import messagebox
import pyperclip
import json

password_generated = ''
# preparing string for password generator
string_for_gen = ''
for i in range(33, 126):
    string_for_gen += chr(i)
print(string_for_gen)

# password generator fuction realisation
def password_generator():
    global password_generated
    password_generated = ''
    if len(entry_website.get()) == 0:
        messagebox.showwarning(title='Warning', message='Do not leave field empty')    
    else: 
                       
        for i in range(1,12):
            index_rand = randint(0, len(string_for_gen)-1)
            password_generated += string_for_gen[index_rand]    
        pyperclip.copy(password_generated)
        lb_gen_password.config(text=password_generated)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_result():
    website = entry_website.get()
    email = entry_email.get()
    if len(password_generated) == 0:
        messagebox.showwarning(title='Warning', message='Do not leave field empty')    
    #building data structure to write into the file
    else:
        data_saved = {
            website:{
                'email' : email,
                'password' : password_generated
            }
        }

        # pop up window to confirm saving 
        confirmation = messagebox.askokcancel(title='Confirmation', message=f"Here are the details you entere: \nEmail: {entry_email.get()}"
            f"\nPassword: {password_generated}\nIs it ok to save?")       
        # save data
        if confirmation:
            try:
                with open('30_day_Exceptions_JSON_Password_manager/Password_Manager/passwords_list.json', 'r') as data_file:
                    data = json.load(data_file)
                    print(data)
                    print('load json')
            except FileNotFoundError:
                with open('30_day_Exceptions_JSON_Password_manager/Password_Manager/passwords_list.json', 'w') as data_file:
                    json.dump(data_saved, data_file, indent=4)
                    print('dump')
            else:
                with open('30_day_Exceptions_JSON_Password_manager/Password_Manager/passwords_list.json', 'r') as data_file:
                    data = json.load(data_file)
                    print('data: ', data)
                    data.update(data_saved)
                with open('30_day_Exceptions_JSON_Password_manager/Password_Manager/passwords_list.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
                    print('update')            
            finally:
                entry_website.delete(0, END)
                lb_gen_password.config(text='')              


# ---------------------------- SEARCH WEBSITE DATA ------------------------------- #







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager by Korotushko')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, bg='white')
logo_img = PhotoImage(file='29_day_Password_manager/logo.png')
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=2 ,row=1)

# Labels
label_web_site = Label(text='Website:') 
label_web_site.grid(column=1,row=2, sticky=E) 

label_email = Label(text='Email/Username:')
label_email.grid(column=1,row=3, sticky=E)

label_password = Label(text='Password:')
label_password.grid(column=1, row=4, sticky=E)

lb_gen_password = Label(width=28, bg='white', anchor='w')  
lb_gen_password.grid(column=2, row=4, sticky=W) 

#Entries
entry_website = Entry(width=33) 
entry_website.grid(column=2, row=2, sticky=W, pady=6)
entry_website.focus()

entry_email = Entry(width=53)
entry_email.grid(column=2, columnspan=2, row=3, sticky=W)
entry_email.insert(0, 'O.Korotushko@gmail.com')

#Buttons
button_gen_password = Button(text='Generate password', width=15, command=password_generator)
button_gen_password.grid(column=3, row=4, padx=5, pady=5, sticky=W)

button_add = Button(text='Add', width=45, command=save_result)
button_add.grid(column=2, columnspan=2, row=5,sticky=W)

button_search = Button(text='Search', width=15) 
button_search.grid(column=3, row=2, padx=5, pady=5, sticky=W) 

window.mainloop()