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
    def datos(self):
        print('La cantidad de llantas es de: ',self.llantas)
        print('El color de la moto es: ',self.color)
        print('El precio de la moto es de: ',self.precio)

class Auto(Fabrica):
    def datos(self):
        print('La cantidad de llantas es de: ',self.llantas)
        print('El color del auto es: ',self.color)
        print('El precio del auto es de:',self.precio)


moto = Moto(2, "Negro", 100000)
moto.datos()

auto = Auto(4, "Grafito", 500000)
auto.datos()
