#TECNICATURA UNIVERSITARIA
#EN PROGRAMACIÓN
#A DISTANCIA
#Práctico 4: Estructuras repetitivas             Alumna Dìaz Monroy Yohanna
 

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

cont=1
while cont<=100:
	print(cont)
cont= cont+1

print("//////////////////////")


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.


numero = int(input("ingrese un numero entero:  "))
i=0
while numero >0:
numero= n//10
i +=1
print (f"el numero tiene {i} digitos")

print("//////////////////////")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

print("introduce el primer numero:  ")
a = int(input())
print (f "El numero introducido es{a}")
print ("introduce el segundo numero:  ")
b= int(input())
print ("el numero introducido es " + str(b))
if a>b:
	mayor=a
	menor=b
else:
	mayor=b
	menor=a
while mayor>=menor:
	suma =suma+mayor
	mayor=mayor-1
print ("la suma es:" +str(suma))



print("//////////////////////")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.


total_acumulado = 0
  
print("Ingrese números enteros para sumar. Ingrese 0 para detenerse.")

  
while True:
    try:
      
entrada = input("Ingrese un número: ")
      
numero = int(entrada)

      
if numero == 0:
        
break  # Salir del bucle si el usuario ingresa 0
      
else:
    total_acumulado += numero
        
print(f"Subtotal acumulado: {total_acumulado}")

    
except ValueError:
      
print("Entrada inválida. Por favor, ingrese un número entero.")

  
print(f"\nTotal acumulado: {total_acumulado}")




print("//////////////")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random

aleatorio= randon.randint(1,100)
while True:
	num=int(imput("ingresa un numero del 1 y 100: ))
	if num==aleatorio:
		print("Felicidades adiviniste el numero ")
	
	elif num<aleatorio:
		print("esta muy abajo, prueba de nuevo")
		print("estas muy arriba, prueba de nuevo")
print ("fin del juego!!!!")


print("//////////////")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.


cont=100
while cont >=0:
	print (cont)
	cont=cont-2

print  ("/////////////////")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

total=0
for i in range(101):
    total=total+i
print("Sumatoria:", total)


print("//////////////")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

def analizar_numeros():
  
 
cantidad_numeros = 100  
# Cambia este valor para probar con menos números

  
numeros = []
  
print(f"Por favor, ingrese {cantidad_numeros} números enteros:")

  
for i in range(cantidad_numeros):
    
while True:
      
	try:
        
entrada = input(f"Ingrese el número {i + 1}: ")
        
numero = int(entrada)
        
numeros.append(numero)
        break  
# Salir del bucle interno si la entrada es válida
      
except ValueError:
        
print("Entrada inválida. Por favor, ingrese un número entero.")

  
pares = 0
  
impares = 0
  
positivos = 0
  
negativos = 0

  
for num in numeros:
    
if num % 2 == 0:
      
pares += 1
    
else:
      
impares += 1

    
if num > 0:
      
positivos += 1
    
elif num < 0:
      
negativos += 1

  

print("\n--- Análisis de los números ingresados ---")
  
print(f"Cantidad de números pares: {pares}")
  
print(f"Cantidad de números impares: {impares}")
  
print(f"Cantidad de números positivos: {positivos}")
  
print(f"Cantidad de números negativos: {negativos}")




print("//////////////")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cant_numeros=100
cont_num =0
sumatoria =0
for cont in range (1, cant_numeros+1):
	print("ingrese numero",cont)
	num= int(input())
	sumatoria = sumatoria + num 
print("el valor promedio es", sumatoria/cont_num)


cantidad_numeros = 100  
# Cambia este valor para probar con menos números

  numeros = []
  print(f"Por favor, ingrese {cantidad_numeros} números enteros:")

  for i in range(cantidad_numeros):
    while True:
      try:
        entrada = input(f"Ingrese el número {i + 1}: ")
        numero = int(entrada)
        numeros.append(numero)
        break 
      except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

  if numeros: 
    suma_total = sum(numeros)
    media = suma_total / len(numeros)
    print(f"\nLa media de los {len(numeros)} números ingresados es: {media}")
  else:
    print("No se ingresaron números para calcular la media.")



print("//////////////")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.



try:
    numero_entero = int(numero)
    numero_str = str(abs(numero_entero))  
	# Convertir a string y manejar negativos
    invertido_str = numero_str[::-1]  
 if numero_entero < 0:
      return -int(invertido_str)         
	    # Agregar el signo negativo si era negativo
    else:
      return int(invertido_str) 

except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")
    return None

# Solicitar al usuario que ingrese un número

entrada_usuario = input("Ingrese un número entero: ")

# Invertir los dígitos del número
numero_invertido = invertir_digitos(entrada_usuario)

# Mostrar el resultado si la inversión fue exitosa
if numero_invertido is not None:
  print(f"El número invertido es: {numero_invertido}")