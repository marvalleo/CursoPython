class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0
    
    @property
    def contador(self):
        return self._contador
    @property
    def cuenta(self):   #Esto es un metodo get
        return self._cuenta
a = A()
#print(a._contador) # Esto es incorrecto porque no se puede acceder a una 
                    #variable privada, se debe usar un metodo get

print(a.cuenta())   # esta es correcta porque se usa un metodo get
                    #pero para poder "quitar" los parentesis se debe usar @property

print(a.cuenta) #acá ya estoy usando @property en vez de parentesis en el metodo get para acceder a la variable privada

    # def incrementar(self):
    #     self._contador += 1
    
    # def cuenta(self):
    #     return self._contador
    
    # def setCuenta(self, valor):
    #     self._contador = valor
    
    # def getCuenta(self):
    #     return self._contador