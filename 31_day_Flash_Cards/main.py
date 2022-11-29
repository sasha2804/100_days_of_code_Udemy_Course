
#-------------------------------GETTING DATA FROM CSV-------------------------------
from email.mime import image
from email.policy import default
import pandas as pd
import random

current_card = {}
to_learn = {}


try:
    data = pd.read_csv('31_day_Flash_Cards/data/to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('31_day_Flash_Cards/data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

#-------------------------------NEXT CARD------------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = 'French', fill='black')
    canvas.itemconfig(card_word, text = current_card['French'], fill='black')
    canvas.itemconfig(canvas_image, image=img_front)
    print(current_card)
    flip_timer = window.after(3000, flip_card)   

#-------------------------------FLIP CARD-------------------------------
def flip_card():
    global trig
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text = current_card['English'], fill='white')
    canvas.itemconfig(canvas_image, image=img_back)
    print(current_card)   
    print('flip card func') 

#-------------------------------REMOVED KNOWN CARDS FROM THE LIST------------------------------
def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv('31_day_Flash_Cards/data/to_learn.csv', index=False)

#-------------------------------SETTING USER INTERFACE-------------------------------
BACKGROUND_COLOR = "#B1DDC6"

from audioop import cross
from tkinter import*
from turtle import back, bgcolor, title, width
window = Tk()
window.title('Flash card by Korotushko')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)


#word card canvas
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file='31_day_Flash_Cards/images/card_front.png')
img_back = PhotoImage(file='31_day_Flash_Cards/images/card_back.png')

canvas_image = canvas.create_image(400,263, image=img_front)
card_title = canvas.create_text(400,150, text='', fill='black', font=('Arial', 30, 'italic'))
card_word = canvas.create_text(400,300, text='', fill='black', font=('Arial', 30, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

#buttons under the card configuration
cross_image = PhotoImage(file='31_day_Flash_Cards/images/wrong.png')
button_unknown = Button(image=cross_image, width=100, height=100, command=next_card)
button_unknown.grid(column=0, row=1)

checker_image = PhotoImage(file='31_day_Flash_Cards/images/right.png')
button_known = Button(image=checker_image, width=100, height=100, command=is_known)
button_known.grid(column=1, row=1)

next_card()

window.mainloop()