letra = input("Ingrese una letra: ")

letra = letra.lower()

# if letra == "a":
#     print("Es vocal")
# elif letra == "e":
#     print("Es vocal")
# elif letra == "i":
#     print("Es vocal")
# elif letra == "o":
#     print("Es vocal")
# elif letra == "u":
#     print("Es vocal")
# else:
#     print("No es vocal")

if letra in "aeiou":
    print("Es vocal")
else:
    print("No es vocal")