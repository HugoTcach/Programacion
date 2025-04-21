# Alumna: Lopez María Laura
# Comisión 16


# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo a
# ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101): # podría ponerse range(101) porque inicia desde 0 por defecto salvo que se aclare de qué posición se quiere partir
    print(i)



# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = abs(int(input("Ingrese un número entero: "))) # abs transforma a un número negativo en positivo, sino el conteo incluye al símbolo - como caracter
longitud = len(str(num)) # str transforma a número en un string para poder ser contado con la función len que solo sirve para caracteres alfabéticos o cadenas 

while str(num) == "":
    num = int(input("Ingrese un número entero: "))
    longitud = len(str(num))

print(f"La cantidad de dígitos del número ingresado es {longitud}")



# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

inicio = min(num1, num2) # al poner un mínimo y máximo ordena automáticamente de menor a mayor sin importar si hay negativos o si se ingresa primero un número mayor y después uno menor
fin = max(num1, num2)
suma = 0

if inicio != fin: # se cumple sólo si los números ingresados son distintos para evitar que el bucle se ejecute innecesariamente, si son iguales no hay número entre ellos y da 0
    contador = inicio + 1 # empieza a contar después del número inicial ya que se pide que no se tenga en cuenta
while contador < fin: # esto excluye al último número porque el bucle se detiene antes de que contador sea igual a fin
    suma += contador # suma lo que vaya avanzando en el contador. Recordar que el contador avanza según pasos indicados (cuenta repeticiones) pero no hace una operación aritmética por sí mismo
    contador += 1 # hace que el contador avance de a uno

print(f"La suma de los números entre {inicio} y {fin} es {suma}")

# La otra opción más simplificada es la siguiente pero no considera posición de los números:

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
suma=0
for i in range(num1+1,num2):
    suma=suma+i

print(f"La suma de los números comprendidos entre {num1} y {num2}, excluyendo a los mismos, es {suma}")



# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total
# acumulado cuando el usuario ingrese un 0.

acumulador = 0
num = int(input("Ingrese un número, si desea terminar ingrese 0: "))

while num != 0: # el bucle se va a cumplir siempre que no ingrese el valor de corte (en éste caso 0)
    acumulador += num # va acumulando los números ingresados representados en la variable num
    num = int(input("Ingrese otro número, si desea terminar ingrese 0: ")) # hay que pedir otro valor, esto se va a iterar siempre que no se ingrese 0, si no se hace éste paso va a sumar infinitamente el primer número ingresado

print("El total acumulado es", acumulador)



# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos 
# fueron necesarios para acertar el número.

import random
num_aleatorio = random.randint(0, 9) # random es la función que me permite la aleatoriedad en un número y randint indica el rango entre paréntesis
intentos = 1 # al poner el 1 se cuenta desde el primer intento que esta antes de empezar el contador en el bucle (intentos +=1)
num_usuario = int(input("Adivina el número de 0 a 9: "))

while num_usuario != num_aleatorio:
    print("Intenta otra vez")
    num_usuario = int(input("Adivina el número de 0 a 9: "))
    intentos += 1

print(f"Acertaste en {intentos} intentos")



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2): # recordar que va en -1 porque tiene que contar de 100 a 0, si pongo 0 cuenta de 100 a 1!!, -2 son los pasos decrecientes, de a 2 marca los pares
    print(i)



# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Ingrese un número positivo: ")) # al aclarar que el número debe ser positivo se evita el error de ingresar un 0, si fuera necesario excluirlo se haría a través de un if (if num >0)
suma = 0 # indica el valor inicial para la variable que acumulará el resultado
for i in range(0, num + 1): # al partir de 0 en realidad cuenta a partir del primer número positivo
    suma += i

print(f"La suma de 1 a {num} es {suma} ")



# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, 
# cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad = 10
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad): 
    num = int(input(f"Ingrese el número {i + 1}: ")) # el i + 1 hace que en la primera iteración muestre el primer número porque contamos a partir de 1 o de -1

    if num % 2 == 0:
        pares +=1 # contador para incrementar de a 1 ya que pregunta cantidades secuenciales
    else:
        impares += 1 

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"De los números ingresados {pares} son pares, {impares} son impares, {negativos} son negativos y {positivos} son positivos")



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el 
# programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cantidad = 100 # éste es el valor único que puede modificarse (para chequeo es mejor probar con una cantidad menor ya que se ingresa número por número)
suma = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i + 1}: ")) # el i + 1 hace que en la primera iteración muestre el primer número porque para un promedio no contamos la posición 0, contamos a partir de 1
    suma += num # acumula los números ingresados y los suma

media = suma/cantidad # cálculo de promedio, siempre fuera del bucle para evitar sumas parciales por cada iteración!

print(f"La media de los valores ingresados es {media}")



# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, 
# el programa debe mostrar 745.

num = input("Ingrese un número")
longitud = len(num) 
for i in range(longitud -1, -1, -1): # con -1 voy recorriendo en sentido inverso, recordar que se cuenta de derecha a izquierda y que al poner -1 va moviendose de a 1 posición "hacia atrás"
    print(num[i], end="") # end= es necesario para que el resultado quede en una sola línea, si no uso el = va a quedar el número en una columna porque end es un salto de línea. Las comillas indican el vacío porque no hay nada adicional
