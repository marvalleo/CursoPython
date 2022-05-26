conjunto = {1 , 2 , 3 , 4 , 5} # "type: set no permite datos repetidos"
lista = [1 , 2 , 3 , 4 , 5] # lista no es un conjunto

print('lista: ',lista)
print(conjunto)

#añadir elementos
conjunto.add(20)
print('prueba añadir:',conjunto)

#eliminar elementos
conjunto.remove(20)
print('prueba añadir:',conjunto)

#convertir a lista
lista = list(conjunto)

#convertir a tupla
tupla = tuple(conjunto)

#convertir a diccionario
diccionario = dict(conjunto)

#convertir a set
conjunto = set(lista)

#Uso de pop, toma una valor al azar y lo elimina
conjunto.pop()
print('prueba pop:',conjunto)

#actualizar un elemento
conjunto.update([1,2,3])

#vacia el conjunto
conjunto.clear()