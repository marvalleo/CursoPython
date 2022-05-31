# Ejercicio 3
# Crear una clase Fabrica que tenga los atributos de Llantas, 
# Color y Precio; luego crear dos clases mas que hereden de Fabrica, 
# las cuales son Moto y Carro. Crear metodos que muestren la cantidad de 
# llantas, color y precio de ambos transportes. Por ultimo, 
# crear objetos para cada clase y mostrar por pantalla los atributos 
# de cada uno

class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    
    def ruedas(self):
        print("Tiene {} ruedas".format(self.llantas))

    def colors(self):
        print("Es de color {}".format(self.color))

    def costo(self):
        print("Cuesta ${}".format(self.precio))
    
class Moto(Fabrica):
    def __init__(self):
        self.llantas = 2
        self.color = "Negro"
        self.precio = 1000000

class Auto(Fabrica):
    def __init__(self):
        self.llantas = 4
        self.color = "Grafito"
        self.precio = 555555555


moto = Moto()
moto.ruedas()
moto.colors()
moto.costo()

auto = Auto()
auto.ruedas()
auto.colors()
auto.costo()
