import turtle
x=int(input("enter number of sides"))
length = int(input("enter the length"))
angle = int(input("enter the angle"))
Turtle = turtle.Turtle()
Turtle.speed(100)
colors = ['red','green','yellow','blue','orange','violet']
#DEMO

def design(a):
    for i in range(a):
        Turtle.color(colors[i])
        if i < a:
            Turtle.forward(length)
            Turtle.right(angle)
        # else:
        #     Turtle.forward(length)
for i in range(1000):
    design(x)
    Turtle.right(13)
