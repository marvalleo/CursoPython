# Ejercicio 1
# Crear una funcion que pida dos numeros. 
# Si el primero es mayor al segundo, 
# el programa debe retornar el valor 1; 
# si el segundo es mayor al primero, debe retornar -1; 
# si ambos son iguales, debe retornar 0

def funcion():
    a= int(input("Ingresa un numero entero: "))
    b= int(input("Ingresa otro numero entero: "))
    x=0
    if a>b:
        x=1
    elif a<b:
        x=-1
    else:
        x=0
    return x

print(funcion())