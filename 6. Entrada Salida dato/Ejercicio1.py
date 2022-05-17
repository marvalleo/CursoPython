import math


a = int(input('Ingrese valor de a: '))
b = int(input('Ingrese valor de b: '))
c = int(input('Ingrese valor de c: '))
x1 = 0
x2 = 0

if ((b*b)-(4*a*c)) < 0:
    print('no se puede realizar')
else:

    x1 =  ((-b) + (math.sqrt((b**2)-(4*a*c))))/(2*a)
    x2 =  ((-b) - (math.sqrt((b**2)-(4*a*c))))/(2*a)
print('Los resultados son: \nX1 = ', x1, '\nX2 = ',x2)