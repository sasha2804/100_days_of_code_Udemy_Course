import imp
from turtle import Screen, Turtle
from paddles import Paddle, Net
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Korotushko Pong Game')
screen.tracer(0)
screen.listen()

paddle_left = Paddle((-350,0))
paddle_right = Paddle((350,0))
net = Net()
ball = Ball()





game_is_on = True

# for i in range(150):
#     ball.move()

while game_is_on:
    time.sleep(0.01)
    ball.move()
    screen.update()
    screen.onkey(paddle_right.move_up,'Up')
    screen.onkey(paddle_right.move_down,'Down')
    screen.onkey(paddle_left.move_up, 'A')
    screen.onkey(paddle_left.move_down,'Y')
    screen.onkey(paddle_left.move_up, 'a')
    screen.onkey(paddle_left.move_down,'y')

    # ball.move()



screen.exitonclick()