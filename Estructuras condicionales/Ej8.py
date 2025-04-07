#Se solicita al usuario que ingrese su nombre y numero segun lo que requiere
nombre=input("Ingrese su noombre:")
#Se pide que ingrese la opcion que desea
print("¿Que opción desea?")
print("1 Todo en mayusculas")
print("2 Todo en minisculas")
print("3 Solo la primera letra en mayuscula")
opcion=input("Ingresa 1, 2 o 3: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opcion incorrecta")