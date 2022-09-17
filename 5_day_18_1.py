from turtle import Turtle, Screen
import turtle
import random as rd

timmy_turtle = Turtle()
screen = Screen()
timmy_turtle.shape("circle")
timmy_turtle.hideturtle()
timmy_turtle.color("green")
screen.colormode(255)

# draw dashed line
# for _ in range(15):
#     timmy_turtle.forward(10)
#     timmy_turtle.penup()
#     timmy_turtle.forward(10)
#     timmy_turtle.pendown()

# draw triangular, square....decagon
# for i in range(3,9):
#     angle = 360/i
#     red = rd.randint(0,255)
#     green = rd.randint(0,255)
#     blue = rd.randint(0,255)
#     colour_code = (red,green,blue)
#     timmy_turtle.pencolor(colour_code)    
#     for j in range(i): 
#         timmy_turtle.forward(100)        
#         timmy_turtle.right(angle)

#random walk
# heading = [90, 180, 270, 360]
# distance = [10, 20, 30]
# timmy_turtle.pensize(5)
# timmy_turtle.speed(0)

# for i in range(150):
#     red = rd.randint(0,255)
#     green = rd.randint(0,255)
#     blue = rd.randint(0,255)
#     colour_code = (red,green,blue)
#     timmy_turtle.pencolor(colour_code)
#     # timmy_turtle.right(rd.choice(heading))
#     timmy_turtle.setheading(rd.choice(heading))
#     timmy_turtle.forward(rd.choice(distance))
   
   


screen.exitonclick()

