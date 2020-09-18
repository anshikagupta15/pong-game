import turtle
import winsound
#basic graphic
win=turtle.Screen()#Screen is a class
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)#stops screen from updating.we do it manually.otherwise game will get slow
#score

score_a=0
score_b=0

#add paddle and ball
#paddle A

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.goto(-350,0)
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
#turtle make drawing when they move we dont want that


#paddle B


paddle_b=turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.speed(0)


#ball


ball=turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.speed(0)
ball.dx=0.1 #change in x coordinate
ball.dy=0.1 #everytime ball move,it moves two pixels


#pen

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0", align="center", font=("courier",24,"normal"))

#function


def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)#set y cord of paddle
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)    
#keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")#on pressing w paddle move up

win.onkeypress(paddle_a_down,"s")#on pressing s paddle move down

win.onkeypress(paddle_b_up,"Up")

win.onkeypress(paddle_b_down,"Down")
#main game loop
while True:
    win.update()#update screen when loop runs everytime


    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #ball will move diagonally
    #border checking
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("pong_sound.mp3",winsound.SND_ASYNC)
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("pong_sound.mp3",winsound.SND_ASYNC)
    if ball.xcor() >390:
        ball.setx(390)
        winsound.PlaySound("pong_sound.mp3",winsound.SND_ASYNC)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b), align="center", font=("courier",24,"normal"))
    if ball.xcor() <-390:
        ball.setx(-390)
        ball.dx *= -1
        winsound.PlaySound("pong_sound.mp3",winsound.SND_ASYNC)
        score_b +=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b), align="center", font=("courier",24,"normal"))
    #ball and paddle collision

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor()+40) and (ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("pong_sound.mp3",winsound.SND_ASYNC)
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor() <paddle_a.ycor()+40) and (ball.ycor()>paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("pong_sound.mp3",winsound.SND_ASYNC)

    
