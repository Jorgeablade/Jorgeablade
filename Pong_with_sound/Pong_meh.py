#Really simple Pong just to learn how turtle and winsound works
#  It has maybe a little bit to much of documentation, but It's a way for me to understand everything, Sorry =(
#  _______  _            _____  _              _        
# |__   __|| |          |  __ \(_)            | |       
#    | |   | |__    ___ | |__) |_   ___  ___  | |  ___  
#    | |   | '_ \  / _ \|  ___/| | / __|/ _ \ | | / _ \ 
#    | |   | | | ||  __/| |    | || (__| (_) || || (_) |
#    |_|   |_| |_| \___||_|    |_| \___|\___/ |_| \___/\[T]/

import turtle #Basic Graphics smoll games :)
import winsound # Try .wav instead of .mp3 if It doesn't work

# Main screen
wn = turtle.Screen() #Make a screen
wn.title("Pong by @ThePicolo") #Top of the window
wn.bgcolor("black")
wn.setup(width=800 ,height=600)
wn.tracer(0) #The screen doesn't refresh instant

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() #Turtle objets 1º trutle (module game), 2ºTurtle (class name) I didn't know ok :|
paddle_a.speed(0) #Animation speed to the max
paddle_a.shape("square") #circle square triagnel etc
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #Default = 20x20 square, this will set the width to 20x5 = 100
paddle_a.penup() #.penup() will lift the turtle off the “digital canvas” and if you move the turtle in penup state it WON'T draw.
paddle_a.goto(-350, 0) #-350 form the mid <--(-) (center) (+) -->

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0) #+350 form the mid <--(-) (center) (+) -->

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0) #+350 form the mid <--(-) (center) (+) -->
ball.dx = 0.25 #Reports the x-increment  the ball moves up right
ball.dy = 0.25 #Reports the y-increment  ^^

# Pen, this is part is use, to make a like a print zone, where the score shows up
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 22, "normal"))


# Funtions
# paddle_a
def paddle_a_up():
    y = paddle_a.ycor() #.ycor return the y cor
    y += 20 #move 20px up
    paddle_a.sety(y) #set the paddle pos on y (set y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 #move 20px down
    paddle_a.sety(y)

# paddle_b
def paddle_b_up():
    y = paddle_b.ycor() #.ycor return the y cor
    y += 20 #move 20px up
    paddle_b.sety(y) #set the paddle pos on y (set y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 #move 20px down
    paddle_b.sety(y)
    
# Keyboard binding
wn.listen() #this line tell the program to listen for keyboards inputs
wn.onkeypress(paddle_a_up, "w") #this will call the funtion paddle_a_up when you press w key
wn.onkeypress(paddle_a_down,"s") #this will call the funtion paddle_a_down when you press s key

wn.onkeypress(paddle_b_up,"Up") #this will call the funtion paddle_sb_up when u press Up key
wn.onkeypress(paddle_b_down,"Down") #this will call the funtion paddle_b_down when u press Down key


#Main game loop
while True:
    wn.update() #everytime the loop goes, It refresh it

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) #The position of the ball move with every refresh, to the right -> by 0.25px because ball.dx = 0.25
    ball.sety(ball.ycor() + ball.dy) #Same but up

    # Top and Bottom Border checking settings
    if ball.ycor() > 290: #290, because since the square is 20x20, like -10 to +10, so when the square hits the border it doesn't go further
        ball.sety(290) #Prevent of going out the border
        ball.dy *= -1 #this reverse the direction, goes down instead of up
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) #Adding a little bit of sound to the bounces

    if ball.ycor() < -290: #Prevent of going down
        ball.sety(-290) #When it's get to the bottom, sets the y to -290
        ball.dy *= -1 #resets the y direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.setx(390) #prevent the ball of getting out
        ball.goto(0, 0) #reset the position of the ball, because it hits de x borders 
        ball.dx *= -1 #this reverse the direction of the ball, just to make it different
        score_a += 1
        pen.clear() #This will clean what we set on the Pen section
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 22, "normal"))

    
    if ball.xcor() < -390:
        ball.setx(390)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 22, "normal"))

    
    # Paddle collission
    if (ball.xcor() > 340 and  ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        #ball collission with the from of the paddle_b, and with the top and bottom of the paddle_b
        ball.setx(340) #When it collides it resets the position, with out this the ball will get bugged
        ball.dx *= -1 #And reverse the direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and  ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)