import turtle
import os
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #speeds up the game

#Score variables
scoreA=0
scoreB=0

#Main loop

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square") #20px by 20px
paddleA.color("white")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square") #20px by 20px
paddleB.color("white")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") #20px by 20px
ball.color("white")
ball.penup()
ball.goto(0,0)

#After paddle movements
ball.dx=0.15
ball.dy=0.15

#Scoring pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center",font=("Courier",24,"normal"))


#Functions

def paddleAUp():
    y=paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleADown():
    y=paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    y=paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y=paddleB.ycor()
    y -= 20
    paddleB.sety(y)

#Keyboard binding

wn.listen()
wn.onkeypress(paddleAUp,"w")
wn.onkeypress(paddleADown,"s")
wn.onkeypress(paddleBUp,"Up")
wn.onkeypress(paddleBDown,"Down")

while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("ballBounce.wav",winsound.SND_ASYNC)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("ballBounce.wav",winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        scoreA += 1
        pen.clear()
        winsound.PlaySound("win.wav",winsound.SND_ASYNC)
        pen.write("Player A: {}  Player B: {}".format(scoreA,scoreB),align="center",font=("Courier",24,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        scoreB += 1
        pen.clear()
        winsound.PlaySound("win.wav",winsound.SND_ASYNC)
        pen.write("Player A: {}  Player B: {}".format(scoreA,scoreB),align="center",font=("Courier",24,"normal"))

    #Colliding with paddles

    if ball.xcor()>340 and (ball.ycor()<paddleB.ycor()+50 and ball.ycor()>paddleB.ycor()-50):
        winsound.PlaySound("ballBounce.wav",winsound.SND_ASYNC)
        ball.dx *= -1

    if ball.xcor()<-340 and (ball.ycor()<paddleA.ycor()+50 and ball.ycor()>paddleA.ycor()-50):
        winsound.PlaySound("ballBounce.wav",winsound.SND_ASYNC) #os.afplay("")
        ball.dx *= -1