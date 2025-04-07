#Crea un input para que el usuario ingrese una contraseña.
contraseña = input("Ingrese una contraseña por favor (entre 8 y 14 caracteres inclusive): ")

#Crea una condicion para que la contraseña tenga entre 8 y 14 carecteres.Si no,muestra un mensaje de "error"
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta!")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 carecteres.")