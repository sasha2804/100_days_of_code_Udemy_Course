from turtle import Turtle

START_POS = [(0,0),(-20,0),(-40,0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake: 
    def __init__(self):
        self.segments = []        
        self.create_snake() 
        self.head = self.segments[0]
        self.head.setheading(0)
        self.head.color('green')
        self.head.speed('slowest')

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)            

            
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def move_snake(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            seg_new = self.segments[seg_num]
            seg_new.goto(new_x, new_y)
          
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)      
  
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())








#   def create_snake(self):
#         for position in START_POS:
#             new_segm = Turtle(shape="square")
#             new_segm.pensize(20)        
#             new_segm.color('yellow')
#             new_segm.penup()
#             new_segm.goto(position)
#             self.snake.append(new_segm)            
#             new_segm.speed('slowest')

#             print(self.snake)
#     def move_snake(self):
#         for seg_num in range(len(self.snake)-1, 0, -1):
#             new_x = self.snake[seg_num-1].xcor()
#             new_y = self.snake[seg_num-1].ycor()
#             seg_new = self.snake[seg_num]
#             seg_new.goto(new_x, new_y)
#             # new_pos = self.snake[seg_num].goto(new_x, new_y)   