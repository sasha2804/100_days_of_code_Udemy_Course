from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(5,1)
        self.goto(position) 

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)        

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Net:
    def __init__(self):
        self.net = Turtle('square')
        self.net.shape('square')
        self.net.color('red')
        self.net.penup()
        self.net.goto(0,-290)
        self.net.pensize(5)
        self.net.shapesize(0.25, 1)
        self.net.setheading(90)
        self.net.hideturtle()
        self.create_net()        

    def create_net(self):
        for i in range(-300,300,40):
            self.net.pendown()
            self.net.forward(20)
            self.net.penup()
            self.net.forward(20)

     
  



