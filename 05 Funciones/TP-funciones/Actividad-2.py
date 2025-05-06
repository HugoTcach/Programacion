#Definir funcion
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Programa principal

nombre_usuario = input("Ingrese su nombre por favor: ")
saludar = saludar_usuario(nombre_usuario)

print(saludar)
