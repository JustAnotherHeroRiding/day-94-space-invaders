from turtle import Turtle
from random import *


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Alien(Turtle):
    def __init__(self,xcoords,ycoords,color):
        super().__init__()
        self.shape('circle')
        self.color(color)
        self.penup()
        self.x = xcoords
        self.y = ycoords
        self.turtlesize(stretch_wid= 1,stretch_len= 1.2, outline= None)
        self.goto(xcoords, self.y)
        self.speed = 6
        self.sleep = 0.04
        self.direction = -1
        self.edge_reached = False
        #self.alien_walk()
        
        
    def alien_walk(self):
        self.x = self.xcor()
        self.x += self.direction*3
        self.goto(self.x, self.ycor())
        #if self.xcor() > 380 or self.xcor() < -380:
            #self.reverse()
        
            
    def reverse(self):
        self.direction = self.direction * -1
        self.y = self.ycor()
        self.y -= 10
        self.x += self.direction *25
        self.goto(self.x,self.y)
        
    
    def fast_move(self):
        self.x = self.xcor()
        self.x -= self.speed
        self.goto(self.x, self.ycor())
        
        if self.xcor() < -380:
            self.go_back()
            
    def go_back(self):
        self.goto(800,self.ycor())
             
        


