from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Korotushko Snake Game')
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        



screen.exitonclick()