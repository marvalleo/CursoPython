# class FabricaTelefonos():
#     marca = "Samsung"

#     def ElaborarHuawei(self):#self
#         return "Huawei"


# telefono = FabricaTelefonos()

# telefono.elaborarHuawei()
# print(telefono.marca)

class FabricaTelefonos():

    def __init__(self, marca, color, memoria, almacenamiento):
        self.marca = marca
        self.color = color
        self.memoria = memoria
        self.almacenamiento = almacenamiento

telefono = FabricaTelefonos('Huawei','Negro',64,128)
print(telefono.marca)
print(telefono.color)