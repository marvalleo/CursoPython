#Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres practicas, el examen parcial y el examen final.' 
#Considere: #PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6 #Donde: P1, P2, P3 : Practicas #PP: promedio de practica #PROM: promedio #EP: examen parcial 


P1 = float(input('Ingrese valor de P1: '))
P2 = float(input('Ingrese valor de P2: '))
P3 = float(input('Ingrese valor de P3: '))
EP = float(input('Ingrese valor de EP: '))
EF = float(input('Ingrese valor de EF: '))
PROM = float()
PP = float()



PP = ( P1 + P2 +P3 ) / 3 
PROM = ( PP + 2*EP + 3*EF)/ 6 
print('El promedio parcial es: ',PP,'\nEl promedio final es : ', PROM)