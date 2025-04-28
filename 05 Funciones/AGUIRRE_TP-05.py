# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!")

# saludar_usuario("Cristian")

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido:")
# edad = int(input("Ingrese su edad: "))
# residencia = input("Ingrese su lugar de residencia: ")

# informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# from math import pi

# def calcular_area_circulo(radio):
#     area_circulo = pi * radio * radio
#     return area_circulo

# def calcular_perimetro_circulo(radio):
#     perimetro_circulo = 2 * pi * radio
#     return perimetro_circulo

# radio = float(input("Ingrese el radio de su circulo: "))

# print(f"El area del circulo es {calcular_area_circulo(radio):.2f} y su perimetro es {calcular_perimetro_circulo(radio):.2f}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# def segundos_a_horas(segundos):
#     return segundos / 3600

# segundos = int(input("Ingrese los segundos a convertir: "))

# print(f"Los segundos ingresados equivalen a aprox.: {segundos_a_horas(segundos):.2f} horas")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")

# numero = int(input("Ingrese un numero y le daré su tabla: "))

# tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# def operaciones_basicas(a, b):
#     return  a + b, a - b, a * b, a / b


# print(f"El resultado de la suma es: {operaciones_basicas(4, 2)[0]}")
# print(f"El resultado de la resta es: {operaciones_basicas(4, 2)[1]}")
# print(f"El resultado de la multiplicación es: {operaciones_basicas(4, 2)[2]}")
# print(f"El resultado de la división es: {operaciones_basicas(4, 2)[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# def calcular_imc(peso, altura):
#     imc = peso / altura
#     return imc

# peso = float(input("Ingrese su peso: "))
# altura = float(input("Ingrese su altura: "))

# print(f"Su índice de masa corporal IMC es {calcular_imc(peso, altura):.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# def celsius_a_fahrenheit(celsius):
#     fahrenheit = celsius * (9 / 5) + 32
#     return fahrenheit

# grados_celsius = float(input("Ingrese los grados Celsius: "))

# print(f"Los grados Celsius ingresados {grados_celsius} equivalen a {celsius_a_fahrenheit(grados_celsius)} Fahrenheit")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a ,b ,c):
     promedio = (a + b +c) / 3
     return promedio

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print("El promedio de los numeros ingresados es: ", round(promedio, 2))