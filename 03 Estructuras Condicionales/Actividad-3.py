#Le pide al usuario que ingrese un número.
numero = int(input("Ingrese un número por favor: "))

#Primero se asegura de que el número sea mayor a 0.Si no es asi,le muestra un mensaje.
if numero > 0:
    #Ahora en esta condicional,confirma si el número ingresado es par o no.
    if numero %2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
else:
    print("El número debe ser mayor que 0")