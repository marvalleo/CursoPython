# Ejercicio 1
# Escribir una tupla con los meses del año, luego, pide al usuario un numero, 
# el que haya ingresado, es el mes que debe mostrar en la tupla

meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

seleccion = int(input('Ingrese un numero de mes: '))

print('Usted seleccionó el mes de: ',meses[seleccion-1])