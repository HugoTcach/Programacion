# Pido el nombre del usuario
nombre = input("Ingresa tu nombre: ")

# Solicito la opción 
print("Selecciona una opción:")
print("1. Mostrar el nombre en mayúsculas")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")
opcion = input("Ingresa 1, 2 o 3: ")

# Transformo el nombre según la opción seleccionada
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida. Por favor, ingresa 1, 2 o 3.")