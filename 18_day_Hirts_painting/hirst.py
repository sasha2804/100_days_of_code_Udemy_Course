from turtle import Turtle, Screen
import turtle
import random as rd
import colorgram

timmy_turtle = Turtle()
screen = Screen()
timmy_turtle.hideturtle()
screen.colormode(255)
timmy_turtle.speed(0)


colours_qty = 25
colors = colorgram.extract('D:/PYTHON/100_coding_challenge/100_days_of_code_Udemy_Course/100_days_of_code_Udemy_Course/18_day_Hirts_painting/image.jpg',colours_qty)
colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_code = (r, g, b)
    colors_list.append(rgb_code)    
list_code = colors_list[5:]


def draw_circle():
    timmy_turtle.dot(20, rd.choice(list_code))

# set starting position
timmy_turtle.penup()
timmy_turtle.setpos(-250, 250)

trig = 1
vert_pos_pitch = 0

while trig < 100:
    for j in range(10):
        trig += 1
        draw_circle()
        timmy_turtle.forward(50)
    vert_pos_pitch += 1
    timmy_turtle.setpos(-250, 250-vert_pos_pitch*50)
    
screen.exitonclick()

