def factorial() :
    from math import factorial
    num = int(input("Ingresa tu numero entero y positivo: ") )
    if num > 0:
        print (factorial(num) )
    else:
        print("El numero es negativo y no podemos proceder")
    factorial( )