# La herencia multiple es una caracteristica que nos permite crear
# clases que heredan de varias clases

class A():
    def primera(self):
        return "Esta es la clase A"

class B():
    def segunda(self):
        return "Esta es la clase B"

class C(A, B):          # Esto es una clase que hereda de A y B
    def tercera(self):  #
        return "Esta es la clase C"


c = C()
print(c.primera())
print(c.segunda())
print(c.tercera())