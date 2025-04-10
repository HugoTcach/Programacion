"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene"""

num = int(input("Ingrese un numero entero: "))
cont = 0
while num > 0:
    num = num // 10
    cont += 1

print(f"El numero ingresado tiene {cont} dígitos")