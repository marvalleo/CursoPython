while True:    # Bucle infinito
    try:#try es un bloque de codigo que puede generar un error
        edad = int(input("Ingrese su edad: "))
        print("Su edad es: ", edad)
        break # Si no se coloca esta linea, el programa seguirá ejecutando
    except ValueError:# Se ejecuta si se produce un error de tipo ValueError
        print("Error, Ingresaste un valor no valido")
    finally:#Este bloque se ejecuta siempre, aunque se haya producido un error o no
        print("Fin del programa")