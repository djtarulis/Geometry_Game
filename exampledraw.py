import turtle
### Create a canvas instance
myturtle = turtle.Turtle()

### Draws a square ###
myturtle.penup()    # literally lift the "pen" so you do not draw during movement
myturtle.goto(50, 75)   # go to a certain coordinate
myturtle.pendown()  # Put pen to canvas to start drawing
myturtle.forward(100)  # pixels of movement
myturtle.left(90)   # degrees of turn
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()
