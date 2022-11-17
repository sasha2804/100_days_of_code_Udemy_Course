# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint

password_generated = ''
# making string for password generator
string_for_gen = ''
for i in range(33, 126):
    string_for_gen += chr(i)
print(string_for_gen)

# making password generator fuction
def password_generator():
    global password_generated
    password_generated = ''    
    if len(entry_website.get()) != 0: #check if website name was entered       
        for i in range(1,12):
            index_rand = randint(0, len(string_for_gen)-1)
            password_generated += string_for_gen[index_rand]    
        print(password_generated)
        lb_gen_password.config(text=password_generated)



# ---------------------------- SAVE PASSWORD ------------------------------- #
save_dict = {'website':{'email': '', 'password': ''}}
data_saved = {}
def save_result():
    if len(password_generated) != 0 and len(entry_website.get()) != 0:
        #building data structure to write into the file
        data_saved[entry_website.get()] = {'email': entry_email.get(), 'password': password_generated}    
        site = entry_website.get()
        login = data_saved[entry_website.get()]['email']
        password = data_saved[entry_website.get()]['password']    
        write_str = f'\n{site}|{login}|{password}'
        with open('29_day_Password_manager/passwords_list.txt', 'a+') as data_file:
            data_file.write(write_str)        
        # cleaning from the screen entry and generated after saving
        entry_website.delete(0, END)
        lb_gen_password.config(text='')


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import*

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
entry_website = Entry(width=53)
entry_website.grid(column=2, columnspan=2, row=2, sticky=W, pady=6)
entry_website.focus()

entry_email = Entry(width=53)
entry_email.grid(column=2, columnspan=2, row=3, sticky=W)
entry_email.insert(0, 'O.Korotushko@gmail.com')

#Buttons
button_gen_password = Button(text='Generate password', width=15, command=password_generator)
button_gen_password.grid(column=3, row=4, padx=5, pady=5, sticky=W)

button_add = Button(text='Add', width=45, command=save_result)
button_add.grid(column=2, columnspan=2, row=5,sticky=W)

window.mainloop()