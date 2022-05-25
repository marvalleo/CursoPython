diccionario = {1 : 2 , 2 : 3 , 3 : 4}

diccionario = {4 : 5 , 6:  7}

print(diccionario)

#diccionario.clear()    Limpia el diccionario

print(diccionario.get(2))  #trae el valor del indice indicado

diccionario.setdefault(4,5)     #recibe valor de llave y valor

diccionario.__setitem__(1,50)        #actualiza valor del diccionario

diccionario.update(diccionario)    #une  los diccionarios, si hay indices repetidos solo quedará uno de ellos

diccionario.copy()  #genera una copia del diccionario

print(diccionario)