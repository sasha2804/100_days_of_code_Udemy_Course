from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color('blue')
        self.speed('fastest')
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x, y)






    def create_snake(self):
        super().create_snake()

        



        new_segm = Turtle(shape="square")
            new_segm.pensize(20)        
            new_segm.color('yellow')
            new_segm.penup()
            new_segm.goto(position)
            self.snake.append(new_segm)            
            new_segm.speed(1)

