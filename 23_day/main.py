import time
from turtle import Screen, Turtle
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

time_delay = 0.35
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
car_manager = CarManager()
scoremanager = Scoreboard()

screen.onkeypress(turtle.move_up, 'Up')

game_is_on = True
while game_is_on:
    if turtle.ycor() >= 240:
        time_delay *= 0.9
        scoremanager.score += 1
        scoremanager.scoreboard()
        turtle.goto(0,-280)        
    for car in car_manager.cars:
        if turtle.distance(car) < 20:            
            scoremanager.crash()
            turtle.color('black')            
            game_is_on = False
    time.sleep(time_delay)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    x = car_manager.ret()   

screen.exitonclick()