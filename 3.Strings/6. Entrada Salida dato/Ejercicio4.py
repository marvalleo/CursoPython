""" Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo> """

nombre = str(input('Ingresa tu nombre: '))
edad = int(input('Ingresa tu edad: '))
sexo = str(input(print('Ingresa tu sexo: ')))

print('Te llamas: ',nombre,'\nTu edad es: ',edad,'\nEres: ',sexo)

# OTRA FORMA ES
print('Te llamas: {}\nTu edad es: {}\nEres: {}'.format(nombre, edad, sexo))

