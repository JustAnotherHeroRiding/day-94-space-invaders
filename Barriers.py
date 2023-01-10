from turtle import Turtle
from random import *


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Barrier(Turtle):
    def __init__(self,xcoords,ycoords,color):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.penup()
        self.y = ycoords
        self.turtlesize(stretch_wid= 1,stretch_len= 2, outline= None)
        self.goto(xcoords, self.y)
        self.durability = 3
             