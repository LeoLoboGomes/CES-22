import turtle

resposta = input ("Por favor diga a quantidade de lados do poligono equilatero a ser desenhado: ")
lados = int (resposta)
angulo = float (360/lados)
wn = turtle.Screen()
alex = turtle.Turtle()
for i in range (lados):
    alex.forward(50)
    alex.left(angulo)
wn.mainloop()