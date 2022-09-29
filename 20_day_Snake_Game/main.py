from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Korotushko Snake Game')
screen.tracer(0)

#head drawing


start_pos = [(0,0),(-20,0),(-40,0)]

segments = []

for position in start_pos:
    new_segm = Turtle(shape="square")
    new_segm.pensize(20)
    new_segm.color("white")
    new_segm.penup()
    new_segm.goto(position)
    segments.append(new_segm)
    new_segm.speed(1)

print(segments)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)
    # segments[0].left(90)


      
        
    



#tail drawing





screen.exitonclick()