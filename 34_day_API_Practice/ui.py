from tkinter import*

THEME_COLOR = "#375362"
FONT_NAME = "Courier"

TEXT_VAR = '0'

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')   
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        # LABELS
        self.label_score = Label(text='Score:', textvariable=TEXT_VAR, bg=THEME_COLOR,font=('Arial', 14, 'bold'),foreground='white')
        # label_score.config(foreground='white')
        # self.label_score.grid(column=1,row=1,pady = 20, padx= 20)
        self.label_score.grid(column=1,row=1, pady=20)

        # CANVAS
        self.canvas = Canvas(width=300, height=250,highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150,125, text='SOME TEXT IS HERE SOME TEXT IS HERE', fill='black', font=('Arial', 20, 'italic'), width=300)
        # self.canvas.grid(column=0 ,row=2, padx = 20, columnspan = 2)
        self.canvas.grid(column=0 ,row=2, columnspan = 2)

        #BUTTONS
        self.true_img = PhotoImage(file='34_day_API_Practice/images/true.png')    
        self.button_start = Button(image=self.true_img, font=FONT_NAME, highlightthickness=0, pady = 0, padx= 0)
        # self.button_start.grid(column=0, row=3, pady = 20, padx= 20)
        self.button_start.grid(column=0, row=3, pady=20)

        self.false_img = PhotoImage(file='34_day_API_Practice/images/false.png')    
        self.button_false = Button(image=self.false_img, font=FONT_NAME, highlightthickness=0, pady = 0, padx= 0)
        # self.button_false.grid(column=1, row=3, pady = 20, padx = 20)
        self.button_false.grid(column=1, row=3, pady=20)

        self.window.mainloop()


    



