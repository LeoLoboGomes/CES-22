import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
angulo = int (360/12)
for i in range (12):
    alex.penup()
    alex.forward(100)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(10)
    alex.stamp()
    alex.back(120)
    alex.left(angulo)
wn.mainloop()