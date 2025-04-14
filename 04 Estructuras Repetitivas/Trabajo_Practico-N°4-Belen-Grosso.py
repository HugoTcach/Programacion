# Ejercicio 1

cont = -1

while cont <= 99:
    cont += 1
    print(cont)

# Ejercicio 2

num = int(input("Ingrese un numero: "))

digitos = 0

while num != 0:
    num = num // 10
    digitos += 1

print(f"La cantidad de digitos es de {digitos}.")

# Ejercicio 3

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))

suma = 0

for i in range(num_1 + 1,num_2,1):
    suma = suma + i

print(f"La suma de los numeros ingresados es de {suma}")

# Ejercicio 4

suma = 0

while (num := int(input("Ingrese un numero entero o '0' para terminar la operacion: "))) != 0:
    suma += num

print(f"El total es de: {suma}")

# Ejercicio 5

import random

total = 0

num_aleatorio = int(random.randint(0, 9))

for i in num_aleatorio:

    num = int(input("Ingrese un numero del 0 al 9: "))
    i += total

print(f"Cantidad de intentos: {total}")

# Ejercicio 6

num_mayor = 100
num_menor = 0

for i in range(num_mayor, num_menor,-1):
    if i % 2 == 0:
        print(i)


# Ejercicio 7

suma = 0

num = int(input("Ingrese un numero positivo: "))

for i in range(1, num):
        suma += i
        
print(f"El total de la suma es: {suma}")


# Ejercicio 8

cont = 0
cont_positivos = 0
cont_negativos = 0
cont_pares = 0
cont_impares = 0

for cont in range (100):
        num = int(input("Ingrese hasta 100 numeros: "))
        if num > 0:
            cont_positivos += 1
        elif num < 0:
            cont_negativos += 1
        # par o impar
        if num % 2 == 0:
            cont_pares += 1
        elif num % 2 > 0:
            cont_impares += 1

print(f"La cantidad de numeros positivos es de {cont_positivos}.")
print(f"La cantidad de numeros negativos es de {cont_negativos}.")
print(f"La cantidad de numeros pares es de {cont_pares}.")
print(f"La cantidad de numeros impares es de {cont_pares}.")


# Ejercicio 9

suma = 0
total = 0

for i in range (100):
        num = int(input("Ingrese hasta 100 numeros: "))
        suma += num

total = suma // 100

print(f"La media de esos valores es de {total}")


# Ejercicio 10

import math

num = int(input("Ingresa un numero: "))
digito = 0
num_invertido = 0

while num > 0:
    digito = num % 10
    num_invertido = num_invertido * 10 + digito
    num = math.trunc(num / 10)

print(f"El numero invertido es: {num_invertido}")