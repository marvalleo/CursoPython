import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

s = turtle.Screen()
s.setup(650, 650)
s.bgcolor('black')
s.title('Proyecto 2')

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape('square')
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = 'stop'
serpiente.color('green')

comida = turtle.Turtle()
comida.shape('circle')
comida.color('yellow')
comida.penup()
comida.goto(0, 100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,-320)
texto.write("Marcador: 0\tMarcador más alto: 0", align="center", font=("verdana",24,"normal"))

texto2 = turtle.Turtle()
texto2.speed(0)
texto2.color('red')
texto2.penup()
texto2.hideturtle()
texto2.goto(0,0)



def arriba():
    serpiente.direction = 'up'


def abajo():
    serpiente.direction = 'down'


def derecha():
    serpiente.direction = 'right'


def izquierda():
    serpiente.direction = 'left'


def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y+20)
    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y-20)
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x+20)
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x-20)


s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")


while True:
    s.update()

    if serpiente.xcor()>300  or serpiente.xcor()<-300 or serpiente.ycor()>300 or serpiente.ycor()<-300:
        texto2.write("PERDISTE !!!", align="center", font=("verdana",40,"bold"))
        time.sleep(2)        
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = 'stop'
        cuerpo.clear()
        texto2.clear()

        marcador = 0
        texto.clear()
        texto.write(f"Marcador: {marcador}\tMarcador más alto: {marcador_alto}", align="center", font=("verdana",24,"normal"))

    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x, y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0, 0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador +=10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write(f"Marcador: {marcador}\tMarcador más alto: {marcador_alto}", align="center", font=("verdana",24,"normal"))

    total = len(cuerpo)
    for index in range(total -1, 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x, y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x, y)

    movimiento()

    for i in cuerpo:
        if i.distance(serpiente)<20:
            texto2.write("PERDISTE !!!", align="center", font=("verdana",40,"bold"))
            time.sleep(2) 
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            texto2.clear()
            marcador = 0
            texto.clear()
            texto.write(f"Marcador: {marcador}\tMarcador más alto: {marcador_alto}", align="center", font=("verdana",24,"normal"))





    time.sleep(retraso)


turtle.done()