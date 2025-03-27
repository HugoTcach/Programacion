# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 

print("Ingrese su nombre:")
nombre = input()
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

print("Ingrese su nombre:")
nombre = input()
print("Ingrese su apellido:")
apellido = input()
print("Ingrese su edad:")
edad = input()
print("Ingrese su lugar de residencia:")
residencia = input()
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 

print("Ingrese el radio:")
radio = int(input())
pi = 3.14
area = pi * radio * radio
perimetro = pi * radio
print(f"El area del circulo es {area} y el perimetro es {perimetro}.")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 

print("Ingrese cantidad de segundos:")

segundos = int(input())
minuto = segundos / 60
hora = minuto / 60

print(f"{segundos} segundos corresponde a {int(hora)} hora/s.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

print("Ingrese un numero:")

numero = int(input())

numero_1 = numero * 1
print(numero_1)
numero_2 = numero * 2
print(numero_2)
numero_3 = numero * 3
print(numero_3)
numero_4 = numero * 4
print(numero_4)
numero_5 = numero * 5
print(numero_5)
numero_6 = numero * 6
print(numero_6)
numero_7 = numero * 7
print(numero_7)
numero_8 = numero * 8
print(numero_8)
numero_9 = numero * 9
print(numero_9)
numero_10 = numero * 10
print(numero_10)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

print("Ingrese un numero distinto de 0:")

num_1 = int(input())

print("Ingrese un segundo numero distinto de 0:")

num_2 = int(input()) 


suma = num_1 + num_2
resta = num_1 - num_2
division = num_1 / num_2
multiplicacion = num_1 * num_2

print(f"La suma es {suma}, la resta es {resta}, la division es {division} y la multiplicacion es {multiplicacion}.")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

print("Ingrese su altura:")
altura = float(input())

print ("Ingrese su peso:")
peso = int(input())

masa_corporal = peso / altura**2

print(f"El IMC es de {int(masa_corporal)}.")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

print("Ingrese una temperatura: ")
celsius = float(input())

fahrenheit = 9/5 * celsius + 32

print(f"El equivalente de {celsius}°C es de {fahrenheit}°F.")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números. 

print("Ingrese tres numeros: ")
n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

promedio = (n_1 + n_2 + n_3) / 3

print(f"El promedio de los tres numeros es de {float(promedio)}.")




