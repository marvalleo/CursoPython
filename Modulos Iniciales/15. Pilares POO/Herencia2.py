#super() es una funcion que nos permite acceder a los metodos de la clase padre

class Animales():
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre)  # super() es una función que nos permite acceder a los metodos de la clase padre
        self.sonido = sonido

perro = Perro("Firulais", "Guau") # Esto es una instancia de la clase Perro
print(perro.nombre)                 
print(perro.sonido)