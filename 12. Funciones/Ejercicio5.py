# Ejercicio 1
# Crear un programa que tenga dos funciones, 
# una que contenga el area de un cuadrado con argumentos de base y altura; 
# y la otra el area de un circulo con argumento de radio


def cuadrado(base, altura):
    area = base * altura
    return area

def circulo(radio):
    area = 3.1416 * radio**2
    return area

base=int(input("Ingrese la base del cuadrado: "))
altura=int(input("Ingrese la altura del cuadrado: "))

print("El area del cuadrado es: ", cuadrado(base, altura))

radio=int(input("Ingrese el radio del circulo: "))
print('El area del circulo es: ',circulo(radio))