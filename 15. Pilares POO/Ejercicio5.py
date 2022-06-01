# Ejercicio 1
# Crear un programa con tres clases Universidad, con atributos 
# nombre (Donde se almacena el nombre de la Universidad). 
# Otra llamada Carerra, con los atributos especialidad 
# (En donde me guarda la especialidad de un estudiante). 
# Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
# El programa debe imprimir la especialidad, edad, nombre y universidad de 
# dicho estudiante con un objeto llamado persona.

class Universidad():
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera():
    def carre(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def est(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print('universidad: {}, carrera: {}, Estudiante: {}, Edad: {}'.format(
            self.Nombre, self.especialidad, self.nombre, self.edad))


persona = Estudiante("Iplacex")
persona.carre("Informática")
persona.est("Marcelo", 45)