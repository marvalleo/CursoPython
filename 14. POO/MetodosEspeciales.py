from glob import escape


class FabricaTelefonos():
    def __init__(self, marca, color):#Constructor, sirve para inicializar los valores
        self.marca = marca    #self se usa para acceder a los atributos de la clase
        self.color = color      #self se usa dentro de la clase
        print("Se ha creado el objeto")

    def __str__(self):#Sirve para mostrar los valores
        return "Marca: {}, Color: {}".format(self.marca, self.color)

    def __repr__(self):#Sirve para mostrar los valores
        return "Marca: {}, Color: {}".format(self.marca, self.color)


    def __del__(self):#Destructor, sirve para borrar los valores
        print("Se ha destruido el objeto")

telefono = FabricaTelefonos('Nokia','Negro')
print(telefono.marca)
print(telefono)

# La respuesta es

# Se ha creado el objeto
# Nokia
# Marca: Nokia, Color: Negro
# Se ha destruido el objeto