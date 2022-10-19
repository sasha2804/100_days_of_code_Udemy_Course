import math

a = 25
b = 45
result = math.atan(a/b)
print(math.degrees(result))

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.turtlesize(1,1)
        self.goto(0,0)


