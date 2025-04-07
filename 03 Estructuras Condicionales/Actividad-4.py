#Defino las constantes.
LIMITE_NINO = 12
LIMITE_ADOLENCENTE = 18
LIMITE_ADULTO_JOVEN = 30

#Le pide al usuario que ingrese su edad.
edad = int(input("Ingrese su edad por favor: "))

#Se asegura de que el número ingresado sea mayor a 0.Si no muestra un mensaje.
if edad > 0:
    #Con condicionales "if" y "elif" va analizando a que categoria pertenece el usuario.
    if edad < LIMITE_NINO:
        print("Usted es un niño")
    elif edad >= LIMITE_NINO and edad < LIMITE_ADOLENCENTE:
        print("Usted es un adolecente")
    elif edad >= LIMITE_ADOLENCENTE and edad < LIMITE_ADULTO_JOVEN:
        print("Usted es un adulto/joven")
    else:
        print("Usted es un Adulto")
else:
    print("La edad debe ser mayor a 0")