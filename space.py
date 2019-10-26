import turtle
import os
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

#Register shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Draw border
borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.color("white")
borderPen.penup()
borderPen.setposition(-300,-300)
borderPen.pendown()
borderPen.pensize(3)
for side in range(4):
	borderPen.fd(600)
	borderPen.lt(90)
borderPen.hideturtle()	

#Set score to 0
score=0
#Draw score
scorePen=turtle.Turtle()
scorePen.speed(0)
scorePen.color("white")
scorePen.penup()
scorePen.setposition(-290,280)
scorestring="Score: %s" %score
scorePen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
scorePen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Choose numebr of enemies
numberOfEnenmies=5
#Create an empty list of enemies
enemies=[]
#Add enemies
for i in range(numberOfEnenmies):
    enemies.append(turtle.Turtle())

#Create enemy
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)

enemyspeed = 7

#Create bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 15

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletState="ready"

#Move the player left and right
def moveLeft():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)
	
def moveRight():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def fireBullet():
    #Make bulletState global
    global bulletState
    if bulletState=="ready":
        bulletState="fire"
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False

#Create keyboard bindings
turtle.listen()
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")
turtle.onkey(fireBullet,"space")

#Main game loop
while True:
    for enemy in enemies:
    #Move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
        if enemy.xcor() > 280:
            for e in enemies:
                y=e.ycor()
                y-=55
                e.sety(y)
            enemyspeed*=-1
        if enemy.xcor() < -280:
            for e in enemies:
                y=e.ycor()
                y-=55
                e.sety(y)
            enemyspeed*=-1
        #Check for collison bw bullet and enemy
        if isCollision(bullet,enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletState="ready"
            bullet.setposition(0,-400)#If enemy reaches the position, it dies
            #Reset the enemy
            enemy.setposition(-200,250)
            x=random.randint(-200,200)
            y=random.randint(100,250)
            enemy.setposition(x,y)
            #Update score
            score+=10
            scorestring="Score: %s" %score
            scorePen.clear()
            scorePen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

        if isCollision(player,enemy):
            player.hideturtle()
            print("Game Over")
            break
    #Move the bullet
    y=bullet.ycor()
    y+=bulletspeed
    bullet.sety(y)

    #Check to see if the bullet reached the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletState="ready"
    
    


delay = input("Press enter to finsh.") #raw_inut() for python 2.7