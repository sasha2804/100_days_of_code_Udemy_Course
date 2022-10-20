from turtle import Screen, Turtle
from paddles import Paddle, Net
from ball import Ball
from score import Score
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

X_LEFT = -30
X_RIGHT = 30
Y_COMMON = 250

score_left = Score((X_LEFT, Y_COMMON))
score_right = Score((X_RIGHT, Y_COMMON))

game_is_on = True
reset_trig = True

screen.onkeypress(paddle_right.move_up,'Up')
screen.onkeypress(paddle_right.move_down,'Down')
# screen.onkey(paddle_right.move_up,'Up')
# screen.onkey(paddle_right.move_down,'Down')
screen.onkeypress(paddle_left.move_up, 'A')
screen.onkeypress(paddle_left.move_down,'Y')
screen.onkeypress(paddle_left.move_up, 'a')
screen.onkeypress(paddle_left.move_down,'y')

while reset_trig:
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        ball.move()
        screen.update()        
        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce_y()    
        if ball.xcor() >= 330 and ball.distance(paddle_right) < 50:
            ball.bounce_x()
        if ball.xcor() <= -330 and ball.distance(paddle_left) < 50:
            ball.bounce_x()
        
        if ball.xcor() > 350: # detect if right paddle misses            
            score_left.score += 1
            score_left.scoreboard()
            ball.ball_reset()
            ball.bounce_x()            
        
        if ball.xcor() < -350: # detect if left paddle misses            
            score_right.score += 1
            score_right.scoreboard()
            ball.ball_reset()
            ball.bounce_x()
            

        
        

    


# while reset_trig:
#     game_is_on = True
#     ball.bounce_x()
#     reset_trig = False





    # ball.move()



screen.exitonclick()