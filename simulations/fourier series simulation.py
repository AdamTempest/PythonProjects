import turtle
import _tkinter
import math
import time

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(0)

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(0)

# set the radius of the circle
radius = 100

def Circle(x,y,r):
    # Move the turtle to the starting position
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw the circle
    t.circle(r)

def vector(cx,cy,x,y):
    # Draw the vector
    t.penup()
    t.goto(cx, cy)
    t.pendown()
    t.goto(x, y)

def drawing():
    while True:
        for angle in range(0, 360):
            # Calculate the x and y coordinates of the vector's end point for both circles using the same angle
            x1 = radius * math.cos(math.radians(angle))
            y1 = radius * math.sin(math.radians(angle))
            x2 = x1+radius * math.cos(math.radians(-angle))
            y2 = y1+radius * math.sin(math.radians(-angle))

            # Draw vectors on both circles
            vector(0,0,x1,y1)
            vector(x1,y1,x2,y2)

            # Update the screen and wait for a short time
            wn.update()
            time.sleep(0.01)

            # Clear vectors on both circles
            t.clear()

            # Draws Circles
            Circle(0,-radius*2,radius*2) # big circle
            Circle(0,-radius,radius)     # base circle
            Circle(x1,y1-radius,radius)  # rotating circle
            
            # Drawing First circle Diameters            
            vector(0,0-radius,0,radius)         # vertical
            vector(-radius,0,radius,0)         # horizontal

            # Drawing Second circle Diameters
            vector(x1,y1-radius,x1,y1+radius)         # vertical
            vector(x1-radius,y1,x1+radius,y1)         # horizontal

            
# Circle(0,-radius,radius)

try:
    # Draw rotating vectors on both circles
    drawing()
except (turtle.Terminator, _tkinter.TclError):
    print("Good Bye.")
    pass

# Keep the window open
wn.mainloop()