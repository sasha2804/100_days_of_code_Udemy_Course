from turtle import Turtle, Screen, color
import random

#1st task drawing lines
# tim = Turtle()
# screen = Screen()
# tim.speed(3)
# def func_forward():
#     tim.forward(5)
# def func_down():
#     tim.forward(5)
# def func_backward():
#     tim.backward(5)
# def func_turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
# def func_turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
# def clear():
#     tim.penup()
#     tim.home()
#     tim.clear()
#     tim.pendown()
# screen.listen()      
# screen.onkeypress(fun = func_forward, key = 'w')
# screen.onkeypress(fun = func_forward, key = 'W')
# screen.onkeypress(fun = func_backward, key = 's')
# screen.onkeypress(fun = func_backward, key = 'S')
# screen.onkeypress(fun = clear, key = 'c')
# screen.onkeypress(fun = clear, key = 'C')
# screen.onkeypress(fun = func_turn_left, key = 'a')
# screen.onkeypress(fun = func_turn_left, key = 'A')
# screen.onkeypress(fun = func_turn_right, key = 'd')
# screen.onkeypress(fun = func_turn_right, key = 'D')
# screen.exitonclick()


screen = Screen()
screen.setup(width = 500, height = 500)
user_bet = screen.textinput(title = 'Make your bet', prompt = 'Enter colour: ')
colors = ['red', 'orange', 'green', 'darkblue']
y_positions = [-135,-45,45,135]
x_position = -225
trig = True
all_turtles = []

for turtle_index in range(0,4):
    new_turle = Turtle(shape = 'turtle')
    new_turle.color(colors[turtle_index])
    new_turle.penup()
    new_turle.goto(x_position, y_positions[turtle_index])
    all_turtles.append(new_turle)

while trig:
    for turtle in all_turtles:
        new_pos = random.randint(1,10)
        x = turtle.pos()        
        if (x[0] + new_pos) > 225:
            turtle.goto(225, x[1])
            trig = False            
            break        
        turtle.forward(new_pos) 

winner_color = turtle.pencolor()
#print(winner_color)

if winner_color == user_bet.lower():
    print('You win')
else:
    print('You lost')
       
screen.exitonclick()