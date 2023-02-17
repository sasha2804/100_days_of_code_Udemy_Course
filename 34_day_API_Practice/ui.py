from cgitb import text
from tkinter import*
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Courier"

TEXT_VAR = '0'

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')   
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        

        # LABELS
        self.label_score = Label(text=f'Score: {self.quiz_brain.score}', bg=THEME_COLOR,font=('Arial', 14, 'bold'),foreground='white') #, textvariable=TEXT_VAR       
        self.label_score.grid(column=1,row=1, pady=20)

        # CANVAS
        self.canvas = Canvas(width=300, height=250,highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150,125, text='SOME TEXT IS HERE SOME TEXT IS HERE', fill='black', font=('Arial', 20, 'italic'), width=300)      
        self.canvas.grid(column=0 ,row=2, columnspan = 2)

        #BUTTONS
        self.true_img = PhotoImage(file='34_day_API_Practice/images/true.png')    
        self.button_start = Button(image=self.true_img, font=FONT_NAME, highlightthickness=0, pady = 0, padx= 0, command=self.check_true_answer)
        self.button_start.grid(column=0, row=3, pady=20)

        self.false_img = PhotoImage(file='34_day_API_Practice/images/false.png')    
        self.button_false = Button(image=self.false_img, font=FONT_NAME, highlightthickness=0, pady = 0, padx= 0, command=self.check_false_answer)
        self.button_false.grid(column=1, row=3, pady=20)

        
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self): 
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    
    def check_true_answer(self):
        if self.quiz_brain.still_has_questions() == True:
            self.quiz_brain.check_answer('True')
            self.get_next_question()
            self.label_score.config(text=f"Score:  {self.quiz_brain.score}")      
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!!!\nYour final score was:\n {self.quiz_brain.score} out of {len(self.quiz_brain.question_list)}")   

    
    def check_false_answer(self):
        if self.quiz_brain.still_has_questions() == True:
            self.quiz_brain.check_answer('False')
            self.get_next_question()        
            self.label_score.config(text=f"Score:  {self.quiz_brain.score}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!!!\nYour final score was:\n {self.quiz_brain.score} out of {len(self.quiz_brain.question_list)}")
        

            


    



