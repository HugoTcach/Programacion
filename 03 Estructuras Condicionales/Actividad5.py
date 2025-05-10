# Pedimos al usuario que ingrese una contraseña
contraseña = input("Ingresa una contraseña: ")

# Si la contraseña contiene entre 8 y 14 caracteres inclusive, es válida
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")