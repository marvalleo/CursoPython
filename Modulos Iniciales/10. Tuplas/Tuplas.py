# la principal caracteristica de las tuplas es que no se pueden modificar
tupla=(1,2,3,4,5)
print('Tipo de la tupla: ',type(tupla))
print(tupla)

#acceder a un elemento de la tupla
print('El elemento 2 de la tupla es: ',tupla[2])

#slice de la tupla
print('El slice de la tupla desde la posicion 1 a la 3 es : ',tupla[1:3])

#convertir tupla a lista
lista = list(tupla)

#concatenar tuplas
tupla2 = (6,7,8)
tupla3 = tupla + tupla2
print('Tupla 3: ',tupla3)




