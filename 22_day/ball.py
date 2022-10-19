import math

# a = 25
# b = 45
# result = math.atan(a/b)
# print(math.degrees(result))

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        self.start = (0,0)
        self.end = (150,150)
        # self.heading = 45        
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.turtlesize(1,1)
        self.goto(0,0)
        self.angle = self.calc_heading()
        self.setheading(self.angle)
  
        
       



    def move(self):        
        self.forward(2)
        print(self.heading())

    def calc_heading(self):
        delta_x = self.end[0] - self.start[0]
        delta_y = self.end[1] - self.start[1]
        result = math.atan(delta_y/delta_x)
        print('result',math.degrees(result))
        return int(math.degrees(result))





