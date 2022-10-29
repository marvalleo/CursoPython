def valores():
    global a, b
    a = 10
    b = 20
    resultado = a+b
    return resultado
# acá termina la funcion valores
print(valores())

resta = a - b #acá(fuera de la función) se usa la variable global, definida en la función valores
print(resta)