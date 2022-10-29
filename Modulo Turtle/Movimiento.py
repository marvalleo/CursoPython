import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.goto(100, 100)
t.goto(-100, 100)
# t.goto(0, 0) vuelve a la posicion inicial
t.home() # otra forma en la que vuelve a la posicion inicial

#haremos un  cuadrado
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)

turtle.done()