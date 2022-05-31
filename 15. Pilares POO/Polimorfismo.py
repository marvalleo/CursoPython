# El polimorfiismo es una característica que permite que una clase pueda
# modificar su comportamiento en función de los valores de sus atributos
#por lo tanto un objeto puede modificar un metodo de la clase padre

class Animales():
    def __init__(self, mensaje): #__init__ es un metodo especial que se ejecuta al instanciar un objeto
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago Guau")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("Guau")#si uso Perro() no se ejecuta el metodo __init__
perro.hablar()

animal = Animales("miau")#si uso Animales() si se ejecuta el metodo __init__
animal.hablar()

pez = Pez("nada")
pez.hablar()