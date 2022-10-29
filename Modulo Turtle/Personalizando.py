import turtle  

s = turtle.Screen()
t = turtle.Turtle()


s.bgcolor("green") # cambia el color de fondo
s.title("Proyecto Tortuga") # cambia el titulo de la ventana

# cambia el tamaño de la tortuga
t.shapesize(3, 3, 3) #ancho, alto, profundidad

t.fillcolor("yellow") # cambia el color de relleno

t.pencolor("white") # cambia el color de la pluma

t.fd(200) # avanza 200 pixeles

t.pensize(5) # cambia el tamaño de la pluma
t.fd(200) # avanza 200 pixeles
turtle.done()