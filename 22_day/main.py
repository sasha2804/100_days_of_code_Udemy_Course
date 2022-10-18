from turtle import Screen, Turtle
from paddles import Paddle, Net

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Korotushko Pong Game')
screen.tracer(0)
screen.listen()


paddle_left = Paddle('left')
paddle_right = Paddle('right')
net = Net()



# create net between players






game_is_on = True
while game_is_on:
    screen.update()
    screen.onkey(paddle_right.move_up,'Up')
    screen.onkey(paddle_right.move_down,'Down')
    screen.onkey(paddle_left.move_up, 'A')
    screen.onkey(paddle_left.move_down,'Y')
    screen.onkey(paddle_left.move_up, 'a')
    screen.onkey(paddle_left.move_down,'y')







screen.exitonclick()