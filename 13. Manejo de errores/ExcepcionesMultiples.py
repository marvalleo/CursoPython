while True:
    try:
        num1 = int(input("Ingrese el primer numero: "))
        resultado = 100 / num1
        print("El resultado es: ", resultado) 
        break
    except ZeroDivisionError:
        print("Error, no se puede dividir entre 0")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print('Su edad es: ', edad)
        break
    except KeyboardInterrupt:#Se ejecuta si se produce un error de tipo KeyboardInterrupt
        print("\nSe ha interrumpido el programa")