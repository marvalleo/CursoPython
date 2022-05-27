# Ejercicio 2
# Escribir una función que reciba una muestra de números 
# en una lista y devuelva su medida.

def medida(*param):
    return len(param)

print(medida(1,2,3,4,5,6,7,8,9,10))