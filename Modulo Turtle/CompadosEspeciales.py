import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10) # velocidad de la tortuga
t.circle(10) # dibuja un circulo de radio 10
t.speed(10)
t.circle(20)
t.speed(10)
t.circle(30)
t.dot(10, "red") # dibuja un punto de color rojo de radio 10

t.hideturtle() # oculta la tortuga
t.speed(1)
t.circle(40)
t.showturtle() # muestra la tortuga
t.circle(100)
t.setx(100)
t.sety(-300)


t.done()