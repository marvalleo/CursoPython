# Ejercicio 1
# Realizar un programa que conste de una clase llamada Estudiante, 
# que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos 
# y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:{} \n Nota:{}".format(self.nombre, self.nota))

    def aprobado(self):
        if self.nota >= 4:
            print(self.nombre, " Ha aprobado")
        else:
            print(self.nombre, " No ha aprobado")


yo = Estudiante("Marcelo", 7)

yo.imprimir()
yo.aprobado()