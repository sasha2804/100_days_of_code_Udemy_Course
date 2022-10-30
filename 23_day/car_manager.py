from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:        
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-220,220))
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.backward(25)   
             
    def ret(self):
        x = len(self.cars)
        return(x)
            

