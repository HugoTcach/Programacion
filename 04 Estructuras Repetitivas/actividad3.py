"""Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores"""

num1 = int(input("Ingrese un valor para num1: "))
num2 = int(input("Ingrese un valor para num2: "))

suma = 0

for i in range(num1 + 1, num2):
    print(i)
    suma += i

print(f"La suma comprendida entre los valores {num1} y {num2} es: {suma}")