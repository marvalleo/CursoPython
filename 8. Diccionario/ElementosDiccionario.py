diccionario = {'Nombre' : "Walter" , 'Apellido' : "Coto" , "Estatura" : 1.8}

print(diccionario)                  #imprime todo el diccionario
print (diccionario . keys( ) )      #imprime los nombre de las "etiquetas"
print (diccionario. values ())      #imprime los valores del diccionario
print(diccionario["Estatura"])      #imprime el valor de la etiqueta indicada

diccionario["Peso"] = "58 kg"       #agrega un nuevo item al diccionario
diccionario["Nombre"] = "Walter"
print(diccionario)