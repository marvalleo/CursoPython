# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad 
# y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


edad = int(input('Ingrese su edad: '))
print(type(edad))
i = 1

while i <= edad:
    if i == 1:
        print('Usted a tenido {} año'.format(i))
    else:
        print('Usted a tenido {} años'.format(i))

    i += 1