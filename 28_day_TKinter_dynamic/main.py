
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔'

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time



# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from turtle import color, width

window = Tk()
window.title('Pomodoro by Korotushko')
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='28_day_TKinter_dynamic/tomato.png')
canvas.create_image(100,112, image=tomato_img)
canvas.create_text(103,130, text='00:00', fill='white', font=(FONT_NAME, 50, 'bold'))
canvas.grid(column=2 ,row=2)

# Labels
label_top = Label(text='Timer', font=('Arial', 24, 'bold'), bg=YELLOW, fg=GREEN)
label_top.grid(column=2, row=0)

label_bottom = Label(text=CHECK_MARK, font=(FONT_NAME, 24, 'bold'), bg=YELLOW, fg=GREEN)
label_bottom.grid(column=2, row=4)

# Buttons
button_start = Button(text='Start', font=FONT_NAME, highlightthickness=0)
button_start.grid(column=1, row=3)

button_reset = Button(text='Reset', font=FONT_NAME, highlightthickness=0)
button_reset.grid(column=3, row=3)



window.mainloop()

