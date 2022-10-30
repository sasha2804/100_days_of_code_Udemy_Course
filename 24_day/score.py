from ctypes import alignment
from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial',12,'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0,280)        
        self.penup()
        self.hideturtle()
        self.color('white')
        self.scoreboard()

    def scoreboard(self):
        self.write(f'Score: {self.score}  High score: {self.high_score}', align=ALIGN, font= FONT) 
    
    def score_print(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.score_print()
    
    def increase_score(self):
        self.score += 1
        self.score_print()
    
    

        

                       
        
