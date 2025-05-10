import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for numero in range(0, 101):
#     print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

# numero = int(input("Ingrese un número entero: "))

# numero = abs(numero)
# digitos = 0

# if numero == 0:
#     digitos = 1
# else:
#     while numero > 0:
#         numero = numero // 10  
#         digitos += 1

# print("El número tiene", digitos, "dígito(s).")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

# inicio = int(input("Ingrese el primer número: "))
# fin = int(input("Ingrese el segundo número: "))

# if inicio > fin:
#     inicio, fin = fin, inicio 

# suma = 0
# numero = inicio + 1 

# while numero < fin:
#     suma += numero
#     numero += 1

# print("La suma de los números entre", inicio, "y", fin, "es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.

# suma = 0
# numero = int(input("Ingrese un número entero (0 para terminar): "))

# while numero != 0:
#     suma += numero
#     numero = int(input("Ingrese otro número (0 para terminar): "))
# print("La suma total es:", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# numero_secreto = random.randint(0, 9)
# intentos = 0
# adivinanza = -1

# print("¡Adivina el número entre 0 y 9!")

# while adivinanza != numero_secreto:
#     adivinanza = int(input("Ingrese su adivinanza: "))
#     intentos += 1

# print(f"¡Correcto! Adivinaste el número {numero_secreto} en {intentos} intento(s).")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

# numero = 100

# while numero >= 0:
#     if numero % 2 == 0:
#         print(numero)
#     numero -= 1

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

# limite = int(input("Ingrese un número entero positivo: "))
# if limite >= 0:
#     suma = 0
#     contador = 0

#     while contador <= limite:
#         suma += contador
#         contador += 1

#     print(f"La suma de los números entre 0 y {limite} es: {suma}")
# else:
#     print("Debe ingresar un número entero positivo.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

# cantidad_numeros = 100  

# pares = 0
# impares = 0
# positivos = 0
# negativos = 0
# contador = 0

# while contador < cantidad_numeros:
#     numero = int(input(f"Ingrese el número {contador + 1}: "))

#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1

#     contador += 1

# print("\nResultados:")
# print(f"Pares: {pares}")
# print(f"Impares: {impares}")
# print(f"Positivos: {positivos}")
# print(f"Negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

# cantidad_numeros = 10  # Usá 100 para el caso real

# suma_total = 0
# contador = 0

# while contador < cantidad_numeros:
#     numero = int(input(f"Ingrese el número {contador + 1}: "))
#     suma_total += numero
#     contador += 1

# media = suma_total / cantidad_numeros

# print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresa un número: ")
numero_invertido = ""

for digito in numero:
    numero_invertido = digito + numero_invertido

print("Número invertido:", numero_invertido)