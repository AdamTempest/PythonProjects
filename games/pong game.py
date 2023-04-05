# This is a simple pong game using turtle

# Import turtle module
import turtle
import keyboard

# Create screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(10)

# Create paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Create paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Create ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1 # Change in x position of ball
ball.dy = 1 # Change in y position of ball

# Create score board
score_a = 0 # Score for player A
score_b = 0 # Score for player B
score = turtle.Turtle() # Turtle object for score display
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Define functions to move paddles up and down
def paddle_a_up():
    y = paddle_a.ycor() # Get current y position of paddle A
    y += 5 # Increase y by 20 pixels
    paddle_a.sety(y) # Set new y position of paddle A
    if paddle_a.ycor() > screen._window_size()[1] / 2: # Check if paddle A goes beyond top boundary
        paddle_a.sety(-screen._window_size()[1] / 2) # Set paddle A to bottom boundary

def paddle_a_down():
    y = paddle_a.ycor() # Get current y position of paddle A
    y -= 5 # Decrease y by 20 pixels 
    paddle_a.sety(y) # Set new y position of paddle A
    if paddle_a.ycor() < -screen._window_size()[1]/2: # Check if paddle A goes beyond bottom boundary
        paddle_a.sety(screen._window_size()[1]/2) # Set paddle A to top boundary

def paddle_b_up():
    y = paddle_b.ycor() # Get current y position of paddle B 
    y += 5 # Increase y by 20 pixels 
    paddle_b.sety(y) # Set new y position of paddle B 
    if paddle_b.ycor() > screen._window_size()[1] / 2: # Check if paddle B goes beyond top boundary
        paddle_b.sety(-screen._window_size()[1] / 2) # Set paddle B to bottom boundary

def paddle_b_down():
    y = paddle_b.ycor() # Get current y position of paddle B 
    y -= 5 # Decrease y by 20 pixels 
    paddle_b.sety(y) # Set new y position of paddle B 
    if paddle_b.ycor() < -screen._window_size()[1]/2: # Check if paddle B goes beyond bottom boundary
        paddle_b.sety(screen._window_size()[1]/2) # Set paddle B to bottom boundary

# Main game loop 
while True:
    screen.update() # Update screen 

    # Move ball 
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy) 

    # Check for border collisions 
    if ball.ycor() > 290: 
        ball.sety(290) 
        ball.dy *= -1 
    
    if ball.ycor() < -290: 
        ball.sety(-290)  
        ball.dy *= -1 
    
    if ball.xcor() > 390:
        ball.dx *= -1  
        score_a += 1  
        score.clear()  
        score.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier",24,"normal")) 
    
    if ball.xcor() < -390:  
        ball.dx *= -1  
        score_b += 1  
        score.clear()  
        score.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier",24,"normal")) 

    # Check for paddle collisions 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50): 
        ball.setx(340) 
        ball.dx *= -1 
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50): 
        ball.setx(-340) 
        ball.dx *= -1

    if keyboard.is_pressed("w"):
        paddle_a_up()
    
    if keyboard.is_pressed("s"):
        paddle_a_down()
    
    if keyboard.is_pressed("Up"):
        paddle_b_up()
    
    if keyboard.is_pressed("Down"):
        paddle_b_down()