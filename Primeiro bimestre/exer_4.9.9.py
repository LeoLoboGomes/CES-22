import turtle

def estrela(t):
    for i in range (5):
        t.forward(100)
        t.right(144)

wn = turtle.Screen()
alex = turtle.Turtle()
estrela(alex)
wn.mainloop()