from turtle import Turtle, Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Korotushko Snake Game')
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()  


screen.exitonclick()