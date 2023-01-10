from turtle import *


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle()
        self.goto(position) 
    def create_paddle(self):
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid= 1,stretch_len= 1, outline= None)
        self.penup()   
    def left(self):
        if self.xcor() > -360:
            newx = self.xcor() - 25
            self.goto(newx, self.ycor())
    def right(self):
        if self.xcor() < 360:
            newxdown = self.xcor() + 25
            self.goto(newxdown, self.ycor())
        