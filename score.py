from turtle import *
ALLIGNMENT = "center"
FONT = ("Courier", 35, 'normal')

class Score(Turtle):
    def __init__(self, position, points):
        super().__init__()
        self.score = -4
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(position)
        self.update_score(points)
        
    
    def update_score(self, points):
        self.clear()
        self.score += points
        self.write(f"{self.score}", align=ALLIGNMENT, font =FONT)

    def update_lives(self):
        self.clear()
        self.score -= 1
        self.write(f"{self.score}", align=ALLIGNMENT, font =FONT)        
    def gameover(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Gameover", align='center', font =FONT)
