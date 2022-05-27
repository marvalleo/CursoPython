# Ejercicio 2
# Escribir una función que reciba un número entero
#  positivo y devuelva su factorial.


def factorial():
    nem = int(input('Ingrese un numero: '))
    i = 1
    j = 1
    while i <= nem:
        j = j * i
        i += 1
    
    print('El factorial de {}! es {}'.format(nem, j))

factorial()


