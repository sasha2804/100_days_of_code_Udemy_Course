import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
car_manager = CarManager()

screen.onkeypress(turtle.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.35)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    x = car_manager.ret()
    print(x)
   


screen.exitonclick()