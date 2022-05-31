# Herencia es una caracteristica que nos permite crear 
# clases que heredan de otras clases


class Animales():
    def camina(self):
        print("Estoy caminando")

    def descripcion(self):
        print("Soy un {}".format(self.animal))

class Perro(Animales):#hereda de animales
    pass # Forma de decirle a python que no haga nada

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

animal = Animales()
animal.camina()

perro = Perro()
perro.camina()

abeja = Abeja("abeja")
abeja.descripcion()

