# Ejercicio 1
# Escribir un programa que pida un numero al usuario 
# y muestre las tablas de multiplicar de ese numero

num = int(input('Ingrese un número: '))
i = 1
mult = 1

while i < 11:
    mult = num * i
    print('{} x {} = {}'.format(i,num,mult))
    i += 1



