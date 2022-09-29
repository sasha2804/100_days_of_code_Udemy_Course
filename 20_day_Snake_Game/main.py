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

print(segments)

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(1)
        screen.update()
        #time.sleep(1)
    



#tail drawing





screen.exitonclick()