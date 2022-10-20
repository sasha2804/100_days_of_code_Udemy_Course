from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        self.start = (0,0)
        self.end = (150,300)              
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10       


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
    
    def ball_reset(self):
        self.goto(0,0)



# import math
# a = 25
# b = 45
# result = math.atan(a/b)
# print(math.degrees(result))

    # def move(self):        
    #     self.forward(2)
    #     # if self.ycor() >= 280:
    #     #     self.setheading(297)

    # def calc_heading(self):
    #     delta_x = self.end[0] - self.start[0]
    #     delta_y = self.end[1] - self.start[1]
    #     result = math.atan(delta_y/delta_x)
    #     print('result',math.degrees(result))
    #     return int(math.degrees(result))





