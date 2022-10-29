import turtle   



# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)

resultado = input("Quiere imprimir una figura? (s/n): ")
if resultado == "s":
    s = turtle.Screen()
    t = turtle.Turtle()
    # hace una figura de un cuadrado
    for i in range(4):
        t.fd(100)
        t.rt(90)

    i = 0
    while i <= 100:
        t.circle(i)
        i += 10
else:
    print("okey")







