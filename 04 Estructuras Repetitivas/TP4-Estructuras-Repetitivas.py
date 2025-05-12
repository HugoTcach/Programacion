#Ejercicio 1: Números del 0 al 100
for i in range(0, 101):
    print(i)

#Ejercicio 2: Cantidad de dígitos de un número entero
numero = input("Ingresa un número entero: ")
print("Cantidad de dígitos:", len(numero.strip("-")))

#Ejercicio 3: Suma de números enteros
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a > b:
    a, b = b, a

suma = 0
for j in range(a + 1, b):
    suma += j

print("La suma es:", suma)

#Ejercicio 4: Secuencia de sumas
CORTE = 0  # Constante para detener el ciclo

sumatoria = 0
numero_ingresado = int(input("Ingrese un número (0 para terminar): "))

while numero_ingresado != CORTE:
    sumatoria += numero_ingresado
    numero_ingresado = int(input("Ingrese otro número (0 para terminar): "))

print("Suma total:", sumatoria)

#Ejercicio 5: Juego con número aleatorio
import random

secreto = random.randint(0, 9)
intentos = 0
acertado = False

while not acertado:
    intento = int(input("Adivina el número (0 a 9): "))
    intentos += 1
    if intento == secreto:
        acertado = True

print("¡Correcto! Lo lograste en", intentos, "intentos.")

#Ejercicio 6: Números pares
for p in range(100, -1, -2):
    print(p)

#Ejercicio 7: Suma desde 0 hasta N
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for h in range(1, n + 1):
    suma += h

print("La suma es:", suma)

#Ejercicio 8: Pares, impares, negativos y positivos
cantidad = 100
pares = impares = positivos = negativos = 0

for c in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#Ejercicio 9: Calcular media de 100 números
cantidad_de_numeros = 100
sumatoria_de_numeros = 0

for b in range(cantidad):
    numero_usuario = int(input("Ingrese un número: "))
    sumatoria_de_numeros += numero_usuario

media = sumatoria_de_numeros / cantidad_de_numeros
print("Media:", media)

#Ejercicio 10: Invertir el orden de los dígitos
numero_al_derecho = input("Ingrese un número: ")
invertido = numero_al_derecho[::-1]
print("Número invertido:", invertido)