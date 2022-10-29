def argumento(*param):#el * indica que se reciben argumentos indefinidos
    return type(param)

print(argumento(10))
print(argumento(10.5))
print(argumento('Hola'))
print(argumento(True))
print(argumento(None))
print(argumento([]))
print(argumento({}))
print(argumento(()))
print(argumento(set()))
print(argumento(range(10)))
