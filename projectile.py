from turtle import *

class Projectile(Turtle):
    def __init__(self, position, owner):
        super().__init__()
        self.create_projectile()
        self.goto(position)
        self.speed(0)
        if owner == 'player':
            self.projectile_speed = 14
        elif owner == 'alien':
            self.color('green')
            self.projectile_speed = -14
        self.sleep = 0.04
        self.projectile_state = "ready"
        self.hideturtle()

        
        
        
    def create_projectile(self):
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid= 1.5,stretch_len= 0.2, outline= None)
        self.penup() 
        
    def fire(self):
        if self.projectile_state == 'ready':
            self.projectile_state = 'fire'
            self.showturtle()
                
    def move(self,owner):
        if self.projectile_state == 'fire':
            y = self.ycor()
            y += self.projectile_speed
            self.goto(self.xcor(), y)
        if owner == 'player':
            if self.ycor() > 280:
                self.projectile_state = "ready"
                self.hideturtle()
        elif owner == 'alien':
            if self.ycor() < -280:
                self.projectile_state = "ready"
                self.hideturtle()
        
    def reset(self):
        self.projectile_state = "ready"
        self.ht()
        self.goto(600,600)
        self.clear()
        
        
        