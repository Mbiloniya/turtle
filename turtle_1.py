import turtle
length = int(input("enter the length"))
angle = int(input("enter the angle"))
Turtle = turtle.Turtle()
Turtle.shape('turtle')
x = 4
# y = 4

Turtle.speed(1)
#FUNCTION
def square(a):
    for i in range(a):
        if i < 3:
            Turtle.forward(length)
            Turtle.left(angle)
        else:
            Turtle.forward(length)

colors = ['red','green','yellow','blue']


for i in range(x):
    Turtle.color(colors[i])
    square(x)
    Turtle.color("Black")
    Turtle.forward(50)
Turtle.goto(0,0)
