import turtle

alex = turtle.Turtle()
wn = turtle.Screen()
alex.pensize(10)
list = [(50,0),(50,-90),(50,-90),(50,-90),(35,-45),(35,-90)]
for (distancia,angulo) in list:
    alex.left(angulo)
    alex.forward(distancia)
alex.penup()
alex.left(45)
alex.forward(40)
alex.left(-90)
alex.forward(50)
alex.left(180)
alex.pendown()
list = [(50,0),(50,-90),(50,-90),(50,-90),(35,-45),(35,-90), (35,0), (35, -90), (35,0), (35, -90)]
for (distancia, angulo) in list:
    alex.left(angulo)
    alex.forward(distancia)
alex.penup()
alex.left(135)
alex.forward(60)
alex.left(90)
alex.forward(50)
alex.left(-45)
alex.pendown()
list = [(35,0),(35,-90),(35,0), (35, -90), (50, -45),(35,-45),(35,-90), (71, -90), (50, 135), (50,90), (50,90), (71, 135)]
for (distancia, angulo) in list:
    alex.left(angulo)
    alex.forward(distancia)
wn.mainloop()