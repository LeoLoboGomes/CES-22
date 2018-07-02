import turtle

def estrela(t):
    for i in range (5):
        t.forward(100)
        t.right(144)

wn = turtle.Screen()
wn.title("Com penup e sem penup")
alex = turtle.Turtle()
for j in range (5):
    estrela(alex)
    alex.penup()
    alex.forward(350)
    alex.right(144)
    alex.pendown()
alex.penup()
alex.back(360)
alex.pendown()
for k in range (5):
    estrela(alex)
    alex.forward(350)
    alex.right(144)
wn.mainloop()