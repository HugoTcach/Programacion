#pylint: disable=missing-module-docstring
import math

#Ejjercicio 1
print("Hola mundo")

# Ejercicio 2
name = input("Introduce tu nombre: ")
print(f"Hola {name}!")  # Más elegante y evita errores de concatenación

# Ejercicio 3
name = input("Introduce tu nombre: ")
surname = input("Introduce tu apellido: ")
age = int(input("Introduce tu edad: "))
country = input("Introduce tu país: ")
print(f"Hola {name} {surname}, tienes {age} años y vives en {country}.")
# Ejercicio 4
#Solitar el radio al usuario
ratio = float(input("Introduce el radio de la circunferencia: "))
#Calcular el área y el perímetro
area= math.pi * ratio ** 2
perimeter = 2 * math.pi * ratio
#Mostrar los resultados con 2 decimales
print(f"El área de la circunferencia es: {area:.2f}")
print(f"El perímetro de la circunferencia es: {perimeter:.2f}")
# Ejercicio 5
seconds = int(input("Introduce los segundos: "))
hours = seconds // 3600
print(f"Horas: {hours}")
# Ejercicio 6
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
# Ejercicio 7
# Programa para operaciones básicas con validación de entradas
# Pedir al usuario dos números enteros distintos de cero
num1 = int(input("Ingrese el primer número entero (distinto de 0): "))
num2 = int(input("Ingrese el segundo número entero (distinto de 0): "))

# Realizar las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division:.2f}")
# Ejercicio 8
# Programa para calcular el IMC
weigth = float(input("Ingrese su peso en kilogramos: "))
height = float(input("Ingrese su altura en metros: "))
imc = weigth / (height ** 2)
print(f"Su índice de masa corporal es: {imc:.2f}")

# Ejercicio 9
celcius=float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit =(9/5) * celcius + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")
# Ejercicio 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
average = (num1 + num2 + num3) / 3
print(f"El promedio de los números es: {average:.2f}")
#terminamos el programa
