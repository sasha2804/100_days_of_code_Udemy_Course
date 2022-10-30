from ctypes import alignment
from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial',12,'normal')
SCORE_FILE = 'E:/Python/git_Udemy_100_days_of_code/100_days_of_code_Udemy_Course/100_days_of_code_Udemy_Course/24_day/my_score.txt' 



class Score(Turtle):
    def __init__(self):
        super().__init__()        
        self.score = 0
        with open(SCORE_FILE) as data:
            self.high_score = int(data.read())
        self.goto(0,280)        
        self.penup()
        self.hideturtle()
        self.color('white')
        self.scoreboard()

    def scoreboard(self):
        self.write(f'Score: {self.score}  Your highest score: {self.high_score}', align=ALIGN, font= FONT) 
    
    def score_print(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(SCORE_FILE, mode = 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.score_print()
    
    def increase_score(self):
        self.score += 1
        self.score_print()
    
    

        

                       
        
