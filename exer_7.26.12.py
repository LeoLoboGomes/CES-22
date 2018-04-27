import turtle

alex = turtle.Turtle()
wn = turtle.Screen()
alex.pensize(10)
list = [(50,0),(50,90),(50,90),(50,90),(71,135),(50,75),(50,120),(71,75)]
for (distancia,angulo) in list:
    alex.left(angulo)
    alex.forward(distancia)
wn.mainloop()