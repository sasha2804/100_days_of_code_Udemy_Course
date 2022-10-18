from turtle import Turtle

pad1_start = [(350,40), (350,20), (350,0), (350,-20), (350,-40)]


class Paddle:
    def __init__(self):
        self.paddle = []
        # self.paddle.speed(0)
        self.create_paddle()


    
    def create_paddle(self):
        for position in pad1_start:
            self.add_segment(position)

        

    def add_segment(self, position):        
        new_segment = Turtle('square')
        
        new_segment.speed(0)
        new_segment.penup()
        new_segment.color('white')
        
        new_segment.goto(position)
        self.paddle.append(new_segment)

        


