# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range(101):
#     print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# numero = int(input("Ingrese un número entero: "))
# cont_digitos = 1
# if numero < 0:
#     numero = -numero

# if numero == 0:
#     cont_digitos = 1
# else:
#     while numero // 10 > 0:
#         numero = numero // 10
#         cont_digitos += 1

# print ("El número ingresado tiene:",cont_digitos, "dígitos.")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# primer_numero = int(input("Ingrese el primer número: "))
# segundo_numero = int(input("Ingrese el segundo número: "))
# suma = 0

# minimo = min(primer_numero, segundo_numero)
# maximo = max(primer_numero, segundo_numero)

# for i in range(minimo + 1, maximo):
#     suma += i

# print("La suma de los números ingresados es:",suma)


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
# suma = 0
# numero = int(input("Ingrese el primer número: "))

# while numero != 0:
#     suma += numero

#     numero = int(input("Ingrese el siguiente número: "))

# print(f"La suma de los números ingresados es: {suma}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# from random import randint

# num_aleatorio = randint(0, 9)
# num_elegido = int(input("Ingrese el número a ver si adivina: "))
# cont_intentos = 1

# if num_elegido == num_aleatorio:
#     cont_intentos = 1
#     print(f"Acertó el número en el intento N° {cont_intentos}!!!!")
# else:
#     while num_elegido != num_aleatorio:
#         num_elegido = int(input("Pruebe con otro número: "))
#         cont_intentos += 1

# print(f"Usted acertó en {cont_intentos} intentos!!!")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(100, -1, -2):
#     print(i)



# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# numero = int(input("Ingrese un número entero positivo: "))
# suma = 0
# if numero >= 0:
#     for i in range(0, numero + 1):
#         suma += i
# else:
#     print("Usted ha ingresado un número equivocado.")
# print("La suma de los números del 0 hasta el", numero,"da:",suma)


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# cont_pares = 0
# cont_impares = 0
# cont_negativos = 0
# cont_positivos = 0

# for i in range(1, 101):
#     numero = int(input("Ingrese un numero: "))
#     if numero % 2 == 0:
#         cont_pares += 1
#     else:
#         cont_impares += 1

#     if numero > 0:
#         cont_positivos += 1
#     elif numero < 0:
#         cont_negativos += 1

# print(f"De los números ingresados hay {cont_positivos} positivos, {cont_negativos} negativos, {cont_pares} pares y {cont_impares} impares ")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# cont = 0
# acum = 0

# for i in range(1, 7):
#     numero = int(input("Ingrese un número: "))
#     cont += 1
#     acum += numero

# media = acum / cont

# print(f"La media de los numeros ingresados es: {media}")
12


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# numero = int(input("Ingrese un número: "))
# invertido= 0

# if numero < 0:
#     numero = -numero

# while numero != 0:
#     ultimo_digito = numero % 10

#     invertido = invertido * 10 + ultimo_digito

#     numero = numero // 10



# print(invertido)


    