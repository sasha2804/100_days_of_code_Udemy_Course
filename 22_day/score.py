from turtle import Turtle   

ALIGN = 'center'
FONT = ('Arial',28,'normal')

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0        
        self.goto(position)        
        self.penup()
        self.hideturtle()
        self.color('white')
        self.scoreboard() 

    def scoreboard(self):
        self.clear()
        self.write(self.score, align=ALIGN, font= FONT)




    
   

    
 
         