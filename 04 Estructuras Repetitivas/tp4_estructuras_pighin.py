
# TP 4 - Estructuras Repetitivas


# 1) Imprimir los numeros del 0 al 100 (uno por linea)
print("Ejercicio 1:")
for i in range(0, 101):
    print(i)

# 2) Contar la cantidad de digitos de un numero ingresado por el usuario
print("\nEjercicio 2:")
numero = input("Ingrese un numero entero: ")
print("Cantidad de digitos:", len(numero.strip("-")))

# 3) Sumar los numeros entre dos valores dados por el usuario (excluyendo los extremos)
print("\nEjercicio 3:")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print("Suma entre los valores (excluidos):", suma)

# 4) Sumar numeros hasta que el usuario ingrese 0
print("\nEjercicio 4:")
total = 0
while True:
    num = int(input("Ingrese un numero (0 para terminar): "))
    if num == 0:
        break
    total += num
print("Total acumulado:", total)

# 5) Juego de adivinar un numero entre 0 y 9
print("\nEjercicio 5:")
import random
oculto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el numero (entre 0 y 9): "))
    intentos += 1
    if intento == oculto:
        break
print("Adivinaste en ", intentos, "intentos!")

# 6) Imprimir todos los numeros pares entre 0 y 100 en orden decreciente
print("\nEjercicio 6:")
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Sumar todos los numeros entre 0 y un numero dado (inclusive)
print("\nEjercicio 7:")
limite = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(0, limite + 1):
    suma += i
print("La suma es:", suma)

# 8) Ingresar 100 numeros y contar pares, impares, positivos y negativos
print("\nEjercicio 8:")
pares = impares = positivos = negativos = 0
cantidad = int(input("Cuantos numeros queres ingresar (ej. 100) "))
for _ in range(cantidad):
    num = int(input("Numero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9) Calcular la media de 100 numeros ingresados
print("\nEjercicio 9:")
total = 0
cantidad = int(input("Cuantos numeros queres ingresar para la media (ej. 100)? "))
for _ in range(cantidad):
    num = int(input("Numero: "))
    total += num
print("Media:", total / cantidad)

# 10) Invertir los digitos de un numero ingresado por el usuario
print("\nEjercicio 10:")
numero = input("Ingrese un numero: ")
if numero.startswith("-"):
    invertido = "-" + numero[:0:-1]
else:
    invertido = numero[::-1]
print("Numero invertido:", invertido)