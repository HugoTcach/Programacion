# Alumna: Lopez María Laura
# Comision 16


# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa 
# principal.

def saludo():
    print("Hola Mundo")

saludo()



# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si 
# se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el 
# nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Por favor ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)

print(saludo)



# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] 
# [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, lugar_residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}"

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Su apellido: ")
edad = input("Su edad: ")
lugar_residencia = input("Lugar de residencia: ")
mensaje = informacion_personal(nombre, apellido, edad, lugar_residencia)

print(mensaje)



# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# Calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y 
# llamar ambas funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
    return math.trunc(math.pi * (radio**2)) # round para redondear los resultados

def calcular_perimetro_circulo(radio):
    return math.trunc(2 * math.pi * radio)

radio = float(input("Por favor, ingrese el radio del círculo: "))

print(f"El área del círculo es {calcular_area_circulo(radio)} y el perímetro es {calcular_perimetro_circulo(radio)}.")



# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas 
# correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    segundos/3600 # una hora son 3600 segundos
    print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas")

segundos = int(input("Ingrese una cantidad de segundos: "))
segundos_a_horas(segundos)



# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima la tabla de multiplicar de ese número 
# del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero}: ")
tabla_multiplicar(numero)



# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    if b == 0:
        return "Error, no se puede dividir por 0"
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    resultado = f"Suma: {suma}, Resta: {resta}, Multiplicacion: {multiplicacion}, Division: {division}"
    return resultado

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultado = operaciones_basicas(a, b)

print(resultado)



# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def operaciones_basicas(a, b):
    if b == 0:
        return "Error, no se puede dividir por 0"
    print(f"{a} + {b} es: ", a + b)
    print(f"{a} - {b} es: ", a - b)
    print(f"{a} * {b} es: ", a * b)
    print(f"{a} / {b} es: ", a / b)
    tupla = tuple
    tupla = (a+b, a-b, a*b, a/b)
    return tupla

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

tup= operaciones_basicas(num1, num2)

print(tup)
print(type(tup)) # define la tupla



# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en 
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_farenheit(celsius):
    return celsius*(9/5)+32

cels = float(input("Ingrese los grados celsius:"))
faren = celsius_a_farenheit(cels)
print(f"{cels}) grados celsius equivalen a {faren} grados farenheit")



# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los 
# números al usuario y mostrar el resultado usando esta función.

import math

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return math.trunc(promedio)

num1 = float(input("ingrese el primer número: "))
num2 = float(input("ingrese el segundo número: "))
num3 = float(input("ingrese el tercer número: "))

resultado = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {resultado}")



