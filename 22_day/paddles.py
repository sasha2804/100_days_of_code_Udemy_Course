from turtle import Turtle


class Paddle:
    def __init__(self, player_side):
        self.paddle = Turtle()
        self.paddle.shape('square')
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.shapesize(5,1)
        self.player_side = player_side
        self.player_side_def(self.player_side)

    def player_side_def(self, player_side):
        if self.player_side == 'left':
            x = -350 
            y = 0
        elif self.player_side == 'right':
            x = 350
            y = 0            
        self.paddle.goto(x, y)

    def move_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)
        

    def move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)


class Net:
    def __init__(self):
        self.net = Turtle('square')
        self.net.shape('square')
        self.net.color('red')
        self.net.penup()
        self.net.goto(0,-290)
        self.net.pensize(5)
        # self.net.shapesize(0.25, 1)
        self.net.setheading(90)
        self.net.hideturtle()
        # self.net.shapesize(0.5)
        # self.create_net()
        self.create_net()
        

    def create_net(self):
        for i in range(-300,300,40):
            self.net.pendown()
            self.net.forward(20)
            self.net.penup()
            self.net.forward(20)
        # self.net.setheading(90)
        # for i in range(-280, 200, 20):
        #     self.net.forward(i)






# from turtle import Turtle

# pad1_start = [(350,40), (350,20), (350,0), (350,-20), (350,-40)]


# class Paddle:
#     def __init__(self):
#         self.paddle = []
#         # self.paddle.speed(0)
#         self.create_paddle()


    
#     def create_paddle(self):
#         for position in pad1_start:
#             self.add_segment(position)

        

#     def add_segment(self, position):        
#         new_segment = Turtle('square')
        
#         new_segment.speed(0)
#         new_segment.penup()
#         new_segment.color('white')
        
#         new_segment.goto(position)
#         self.paddle.append(new_segment)

        


