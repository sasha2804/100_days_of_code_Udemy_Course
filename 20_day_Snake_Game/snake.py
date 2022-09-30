from turtle import Turtle

START_POS = [(0,0),(-20,0),(-40,0)]
STEP = 20

class Snake: 
    def __init__(self):
        self.snake = []        
        self.create_snake()
    def create_snake(self):
        for position in START_POS:
            new_segm = Turtle(shape="square")
            new_segm.pensize(20)
            new_segm.color('white')
            new_segm.penup()
            new_segm.goto(position)
            self.snake.append(new_segm)            
            new_segm.speed(1)
            print(self.snake)
    def move_snake(self):
        for seg_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(STEP)
        




    