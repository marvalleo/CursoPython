class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0
    
    @property
    def contador(self):
        return self._contador

    @contador.setter
    def contador(self, valor):
        self._contador = valor

    @property
    def cuenta(self):   #Esto es un metodo get
        return self._cuenta

    @cuenta.setter
    def cuenta(self, valor):   #Esto es un metodo set
        self._cuenta = valor

a = A()

print(a.cuenta) #acá ya estoy usando @property en vez de parentesis en el metodo get para acceder a la variable privada
a.cuenta = 20   #Esto es correcto porque se usa un metodo set
print(a.cuenta)

print(a.contador)
a.contador = 50
print(a.contador)