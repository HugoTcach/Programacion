### Práctico 4: Estructuras repetitivas

## Actividad 1
for i in range(0,101):
    print(i)

## Actividad 2
num = input("Escriba un número entero")
print(f"El número ingresado tiene {len(num)} dígitos.")

## Actividad 3
print("Ingrese dos números")
n = int(input())
m = int(input())
if n < m:
    num_menor = n
    num_mayor = m
else:
    num_menor = m
    num_mayor = n
suma_total = num_menor + 1
for num_menor in range(num_menor + 1, num_mayor):
    suma_total = suma_total + (num_menor + 1)
    # print(num_menor)
print(suma_total - num_mayor)

## Actividad 4
print("Ingrese un número entero:")
num = int(input())
num_2 = num
while num_2 != 0:
    print(num)
    num_2 = int(input(print("Ingrese otro número para sumarlo al anterior o marque 0:")))
    num = num + num_2

## Actividad 5
import random
num = random.randint(0, 9)
print("Adivina el número entre el 0 y el 9")
cont = 0
while num_2 != num:
    num_2 = int(input(print("Intente un número: ")))
    cont += 1
print(f"Adivinaste!. El número era {num}. Te tomaron {cont} intentos")

## Actividad 6
i = 100
for i in range (100, -1, -2):
    print(i)

## Actividad 7
print("Ingrese un número entero positivo:")
num = int(input())
suma_total = num
while num < 0:
    print("Error, el número ingresado es negativo.")
else:
    for num in range(num, -1, -1):
        suma_total = suma_total + (num - 1)
print(suma_total - num + 1)

## Actividad 8
print("Ingrese hasta cien números")
cant_max = 100
cont_pos = 0
cont_neg = 0
cont_par = 0
cont_impar = 0
while cant_max > 0:
    num = int(input("Ingrese un número:"))
    cant_max -= 1
    if (num % 2 == 0) or (num == 0): # Cero es parte de los números pares, lo agrego en la condición.
        cont_par += 1
    else:
        cont_impar += 1

    if num > 0:
        cont_pos += 1
    elif num < 0:  
        cont_neg += 1
print(f"La cantidad de números pares ingresados fueron {cont_par}, la cantidad de números impares fueron {cont_impar}, la cantidad de números positivos fueron {cont_pos} y la cantidad de números negativos fueron {cont_neg}.")

## Actividad 9
print("Ingrese hasta cien números para conseguir su media.")
cant_max = 100
cont = cant_max
suma_total = 0
while cont > 0:
    p = input("Ingrese un número, o marque S para salir: ")
    if (p != "S") and (p != "s"):        # Si no se ingresa S o s, se sigue pidiendo números. Una forma para cortar el bucle.
        p = int(p)
        suma_total = suma_total + p
        cont -= 1
        print(cont)
    else:
        cont = 0
print(f"La media de los números ingresados es: {suma_total / cant_max}")

## Actividad 10
print("Ingrese un número para invertir su orden")
num = int(input())
inver = ""
while (num > 0) or (num < 0):
    digito = num % 10
    num = num // 10
    inver = inver + str(digito)
print(f"El número invertido es: {inver}")