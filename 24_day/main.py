from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

file = open('my_score.txt')

content = file.read()

print(content)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game Korotushko')
screen.tracer(0)
screen.listen()

LIM = 280

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_print()      
        
# detect collistion with wall
    if snake.head.xcor() > LIM or snake.head.xcor() < -LIM or\
        snake.head.ycor() > LIM or snake.head.ycor() < -LIM:
        score.reset()
        snake.reset()
# detect collision with tail
# if head collides with any segment in the tail:
# trigger game_over
    for segment in snake.segments[1:-1]:        
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()