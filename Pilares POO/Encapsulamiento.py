class A():                 #Encapsulamiento es una caracteristica que nos permite 
    def __init__(self):       #ocultar los detalles de nuestra clase
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self._contador = 0     #Esto es una forma de encapsular una variable
                                #que no queremos que se vea en el exterior
    def incrementar(self):      #con  guion bajo se encapsula por fuera de la clase
        self._contador += 1
        
    def cuenta(self):
        return self._contador

print("Objeto 1")
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
#print(a.contador)#Esto no se puede hacer porque el contador es privado

print("Objeto 2")
b = A()
print(b.cuenta())
b.incrementar()
print(b.cuenta())