class A():
    def __init__(self):
        self._contador = 0       #Esto es una forma de encapsular una variable
        self.cuenta = 0
    
    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

a = A()
print(a.cuenta) #Esto no se puede hacer porque el contador es privado
               #lo correcto es unsar un metodo get
a.cuenta = 20   #Esto no es correcto porque no se puede cambiar el valor de una variable privada
                #en este caso se debe usar un metodo set
print(a.cuenta)