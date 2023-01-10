#Using Python Turtle, build the classic shoot 'em up game -
# space invaders game.

#Space Invaders Wikipedia Page

#Your space ship can move left and right and it can hit 
# some alien ships. Every second the aliens will move closer 
# to your ship. Once the aliens touch your ship then it's game 
# over. There are usually some barriers between you and the 
# aliens which offers you defensive positions.

#You can play the game here:

#https://elgoog.im/space-invaders/

#Lets build it using Turtle and then with PyGame 


#Steps
#Create the window DONE
#Create the player, can move left and right and shoot upwards DONE
#create the invaders DONE
#2 rows of 10 point enemies, 2 rows of 20 points Created each type with a different color
#1 row on top of 30 points
#spaceship that flies fast above the other enemies DONE

#the spaceship respawns even if it was killed and can appear multiple times per round DONE

#Scoreboard DONE
#On colision with the projectile remove the enemy and projectile,increase the score DONE

#Barriers that block shots and protect the player DONE

#The invaders shoot downwards towards the player DONE

#need colision now for the enemy shots DONE
#if the player gets hit lose 1 live DONE


#If their shot and the player shot collide, delete both and increase score DONE

#Space invaders move left and right and after hitting the edge go down
#11 enemies per row


from turtle import *
from time import sleep
import numpy as np
from player import Player
from projectile import Projectile
from invaders import Alien
import random
from score import Score
from Barriers import Barrier

def fire_projectile():
    global rocket
    if "rocket" in globals() and rocket.projectile_state != "ready":
        return
    # Create the projectile
    rocket = Projectile((player.xcor(), player.ycor() + 30), 'player')
    # Fire the projectile
    rocket.fire()
    rocket.color('orange')
    #rocket.projectile_state = 'fire'
    
    

COLORS = ["red", "orange", "yellow", "green", "purple", "brown", "white", \
    "pink", "lightblue", "lightgreen"]


aliens = []
barriers = []
lasers = []
withoutspaceship = []

screen= Screen()
screen.setup(width = 800,height= 600)

screen.bgcolor('black')
screen.title("Space Invaders")
screen.tracer(0)



player = Player((0, -250))
#rocket = Projectile((player.xcor(), player.ycor() +30))


scoreboard = Score((330,230), 4)
lives = Score((-360,-280), 3)
lives.update_score(4)



screen.listen()
screen.onkey(player.left,"Left")
screen.onkey(player.right,"Right")

screen.onkey(fire_projectile, "Up")

rowcolor = ''

for x in list(np.arange(-230,230,45)):
    for y in range(120, 241, 30):
        if y == 120 or y == 150:
            rowcolor = COLORS[0]
        if y == 180 or y == 210:
            rowcolor = COLORS[1]
        if y == 240:
            rowcolor = COLORS[6]
        alien= Alien(x, y,rowcolor)
        aliens.append(alien)
        withoutspaceship.append(alien)
        

for x in list(np.arange(-320,340,160)):
    for y in range(-120, -20, 30):
        barrier = Barrier(x,y,'white')
        barriers.append(barrier)
        
#Lets change color after the first hit
        
spaceship = Alien(800, 280 , 'green')
#AHHHH so the spaceship is blocking me
aliens.append(spaceship)

game = True
while game:
    screen.update()
    sleep(spaceship.sleep)
    spaceship.fast_move()
    for alien in withoutspaceship:
        for barrier in barriers[:]:
                if alien.distance(barrier) < 22:
                    barrier.durability == 0
                    barrier.hideturtle()
                    barriers.remove(barrier)
        if alien.distance(player) < 22 or alien.y < -280:
            lives.clear()
            game= False
            scoreboard.gameover()
        if alien.x < -380:
                print(alien.x)
                for alien in withoutspaceship:
                    alien.reverse()
        if alien.x > 380:
            print(alien.x)
            print(alien.xcor())
            for alien in withoutspaceship:
                alien.reverse() 
    for alien in aliens:
        alien.alien_walk() 
    
            
        if random.randint(1,1000) == 5:
            laser = Projectile((alien.xcor(), alien.ycor() + 30), 'alien')
            # Fire the projectile
            laser.fire()
            laser.color('green')
            lasers.append(laser)
            
    if 'laser' in globals():
        for laser in lasers:
            laser.move('alien')
            if 'rocket' in globals():
                if laser.distance(rocket) < 20:
                    laser.reset()
                    rocket.reset()
            for barrier in barriers[:]:
                if laser.distance(barrier) < 22:
                    laser.reset()
                    barrier.durability -= 1
                    #print(barrier.durability)
                    if barrier.durability == 2:
                        barrier.color("orange")
                    elif barrier.durability == 1:
                        barrier.color("red")
                    elif barrier.durability == 0:
                        barrier.hideturtle()
                        barriers.remove(barrier)
            if laser.distance(player) < 20:
                laser.reset()
                lives.update_lives()
            
        
    if 'rocket' in globals():
        #sleep(rocket.sleep)
        rocket.move('player')
        
        for barrier in barriers[:]:
            if rocket.distance(barrier) < 22:
                rocket.reset()
                barrier.durability -= 1
                #print(barrier.durability)
                if barrier.durability == 2:
                    barrier.color("orange")
                elif barrier.durability == 1:
                    barrier.color("red")
                elif barrier.durability == 0:
                    barrier.hideturtle()
                    barriers.remove(barrier)
                
            
    
        for alien in aliens[:]: 
            if rocket.distance(alien) < 20:
                #print("It's a hit")
                alien.ht()
                aliens.remove(alien)
                #print(tile.color())
                
                if alien.color() == ('red', 'red'):
                    scoreboard.update_score(10)
                elif alien.color() == ('orange', 'orange'):
                    scoreboard.update_score(20)
                elif alien.color() == ('white', 'white'):
                    scoreboard.update_score(30)
                elif alien.color() == ('green', 'green'):
                    scoreboard.update_score(50)
                
                rocket.reset()
                
    if len(withoutspaceship) == 0 or lives.score == -1:
        lives.clear()
        game= False
        scoreboard.gameover()
                        






screen.exitonclick()