
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    label_top.config(text='Timer')
    label_bottom.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps    
    reps += 1
    work_reps = (1,3,5,7)
    pause_reps = (2,4,6)
    if reps%8 == 0:
        print('15 min reps',reps)       
        count_down(90)
        label_top.config(text='Break', fg=RED)
    elif reps in work_reps:
        print('20 min reps',reps)       
        count_down(60)
        label_top.config(text='Work', fg=GREEN)            
    elif reps in pause_reps:
        print('5 min reps',reps)         
        count_down(30)
        label_top.config(text='Break', fg=PINK)  
 # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = count//60
    if minutes < 10:
        minutes = '0'+str(minutes)    
    seconds = count%60
    if seconds < 10:
        seconds = '0'+str(seconds)        
    timer_out = f'{minutes}:{seconds}'
    canvas.itemconfig(timer_text, text=timer_out)   
    if count > 0:    
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()        
        if reps%2 == 0:
            print('mark and reps: ', reps)       
            check_mark = label_bottom.cget('text') + '✔'              
            label_bottom.config(text= check_mark)
 # ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title('Pomodoro by Korotushko')
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='28_day_TKinter_dynamic/tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(103,130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=2 ,row=2)

# Labels
label_top = Label(text='Timer', font=('Arial', 50, 'bold'), bg=YELLOW, fg=GREEN)
label_top.grid(column=2, row=0)

label_bottom = Label(font=(FONT_NAME, 24, 'bold'), bg=YELLOW, fg=GREEN)
label_bottom.grid(column=2, row=4)

# Buttons
button_start = Button(text='Start', font=FONT_NAME, highlightthickness=0, command=start_timer)
button_start.grid(column=1, row=3)

button_reset = Button(text='Reset', font=FONT_NAME, highlightthickness=0, command=reset_timer)
button_reset.grid(column=3, row=3)

window.mainloop()

