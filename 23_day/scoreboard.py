from turtle import Turtle

FONT = ("Courier", 14, "normal")
ALIGN = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.scoreboard()

    def scoreboard(self):        
        self.clear()
        self.write(f'Level: {self.score}', align=ALIGN, font= FONT) 

    def crash(self):
        self.clear()
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGN, font= FONT)




