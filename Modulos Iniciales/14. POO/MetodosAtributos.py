class FabricaTelefonos():
    marca = "Samsung"
    color = "Negro"
    memoria = 32
    almacenamiento =128

    def llamar(self, mensaje):
        return mensaje

    def musica(self):
        print('Estas escuchando musica')

telefono = FabricaTelefonos()
print(telefono.marca)
print(telefono.color)
print(telefono.memoria)
print(telefono.almacenamiento) 

telefono.llamar("Hola")
telefono.musica()