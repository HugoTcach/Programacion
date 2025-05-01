#Definir funciones
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}"

#Programa principal
nombre = input("Ingrese su nombre por favor: ")
apellido = input("Ingrese su apellido por favor: ")
edad = input("Ingrese su edad por favor: ")
residencia = input("Ingrese su lugar de residencia por favor: ")

print(informacion_personal(nombre, apellido, edad, residencia))