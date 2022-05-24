#Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. 
#El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

vocal = str(input ('Insertar vocal en minuscula: '))
letra = str(input ('Insertar letra en mayuscula: '))

#print('Letra:',str.lower(letra),'\nVocal: ',str.upper(vocal))
vocal = vocal.upper()
letra = letra.lower() 


print('Letra:',letra,'\nVocal: ',vocal)