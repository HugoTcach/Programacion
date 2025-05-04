import utils
#Funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#Principal
nombre = input("Ingrese su nombre: ").title()
apellido = input("Ingrese su apellido: ").title()
edad = utils.get_num("Ingrese su edad: ")
residencia= input("Ingrese su residencia: ").title()
informacion_personal(nombre, apellido, edad, residencia)