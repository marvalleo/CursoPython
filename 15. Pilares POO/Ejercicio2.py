# Ejercicio 2
# Realizar un programa en el cual se declaren dos valores enteros 
# por teclado utilizando el método __init__. Calcular después la suma, 
# resta, multiplicación y división. Utilizar un método para cada una 
# e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingrese el primer valor:"))
        self.num2 = int(input("Ingrese el segundo valor:"))
    
    def suma(self):
        self.suma = self.num1 + self.num2
        return "La suma es de: {}".format(self.suma)

    def resta(self):
        self.resta = self.num1 - self.num2
        return "La resta es de: {}".format(self.resta)

    def multiplicacion(self):
        self.mult = self.num1 * self.num2
        return "La Multipicación es de: {}".format(self.mult)

    def division(self):
        self.div = self.num1/self.num2
        if self.num2 == 0:
            return "No se puede dividir por 0"
        else:
            return "La division es de: {}".format(self.div)
    
calc = Calculadora()
print(calc.suma())
print(calc.resta())
print(calc.multiplicacion())
print(calc.division())
