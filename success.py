import turtle

def draw_circle(turtle,color,size,x,y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

Turtle = turtle.Turtle()
Turtle.shape('turtle')
Turtle.speed(7)

draw_circle(Turtle,'green',50,0,0)

Turtle.penup()
Turtle.goto(0,-50)
Turtle.color('green')
Turtle.write("Great job")
Turtle.goto(0,-120)

