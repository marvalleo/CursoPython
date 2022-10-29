# Ejercicio 1
# Crear un programa que tenga una lista, 
# luego crear una funcion con la cual se van a pedir 
# numeros al usuario para agregar a la lista. 
# Debes crear una segunda funcion en donde se ordenen 
# los numeros pares e impares dentro de dos listas nuevas

lista = [1,2,3,4,5]

def agregaNumeros():
    num = int(input('Ingrese un numero: '))
    lista.append(num)
    eleccion = input('Quiere agregar otro numero? (y/n)')
    if eleccion == 'y':
        agregaNumeros()
            
8
def ordenaListas():
    pares = []
    impares = []

    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    
    print('Lista de pares: ',pares)
    print('Lista de impares: ',impares)

agregaNumeros()
ordenaListas()



