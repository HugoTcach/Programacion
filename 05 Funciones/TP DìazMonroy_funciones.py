
#TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
# Práctico 2: Funciones en Python
# Alumna : Díaz Monroy Yohanna

# Actividades :



# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el 
# mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

nombre = input("coloca la palabra mundo")
print( f"hola {nombre}")

print ################


#  2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un 
# nombre y devuelva un saludo personalizado.Por ejemplo, si se llama con 
# saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa 
# principal solicitando el nombre al usuario.


# Definicion de funciones 
nombre = input ("Coloca tu nombre:  ")
print(f"Hola {nombre}")

print ################

#3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos 
# al usuario y llamar a esta función con los valores ingresados.

# funcion informacion personal 
nombre = input ("Coloca tu nombre:  ")
apellido = input ("Coloca tu apellido:  ")
edad = input ("Coloca tu edad:  ")
residencia = input ("Coloca tu residencia:  ")

print(f"Soy {nombre}")
print(f"mi apellido es {apellido}")  
print(f"mi edad es {edad} años")
print(f"Y vivo en {residencia}")

print ################

#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como
#  parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#A = π r²
# P = 2 * r * π
#funcion area
radio = int(input("ingrese radio:   "))
area = 3,1416*(radio*radio)
perimetro = 2*radio*3,1416

# Programa principal
print (f"el area del circulo es{area}, el perimetro del  circulo es {perimetro}")

print ###########

#  5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de 
# segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#Definicion de funciones
segundos = int(input("ingreses segundos:  "))
segundos_a_horas = segundos // 60

# Programa principal
print (f"la cantidad en horas es {segundos_a_horas}")


print ################

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un 
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.


def tabla_multiplicar(numero):
  
  print(f"Tabla de multiplicar del {numero}:")
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Pedir al usuario el número
try:
  num_str = input("Ingrese un número entero para ver su tabla de multiplicar: ")
  numero = int(num_str)

  # Llamar a la función
  tabla_multiplicar(numero)

except ValueError:
  print("Error: Por favor, ingrese un número entero válido.")



print ################

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números 
# como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, 
# multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
  
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  if b == 0:
    division = None
  else:
    division = a / b
  return (suma, resta, multiplicacion, division)

# Solicitar los números al usuario
try:
  num1_str = input("Ingrese el primer número: ")
  num2_str = input("Ingrese el segundo número: ")
  numero1 = float(num1_str)
  numero2 = float(num2_str)

  # Llamar a la función
  resultados = operaciones_basicas(numero1, numero2)

  # Mostrar los resultados de forma clara
  print(f"\nResultados de las operaciones con {numero1} y {numero2}:")
  print(f"Suma: {resultados[0]}")
  print(f"Resta: {resultados[1]}")
  print(f"Multiplicación: {resultados[2]}")
  if resultados[3] is not None:
    print(f"División: {resultados[3]}")
  else:
    print("División: No se puede dividir por cero.")

except ValueError:
  print("Error: Por favor, ingrese valores numéricos válidos.")


print ################

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la 
# altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos 
# y llamar a la función para mostrar el resultado con dos decimales.


def calcularIMC(p,a):
    return p/(a*a)



peso = float(input("ingrese su peso:   "))
altura = float(input("ingrese su altura:   "))
print(f"su indice de masa corporal es {calcularIMC(peso,altura)}")


print ################

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados 
# Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y 
# mostrar el resultado usando la función.



def convertir(c):
    return (c * 9/5) + 32

n = float(input("ingrese grados celsius:  "))
print (f"la conversion de grados celsius a fahrenheit es {convertir(n)}")

print ################

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
# y devuelva el promedio de ellos.Solicitar los números al usuario y mostrar el resultado usando
#  esta función

def promedio(a,b,c):
    return (a + b + c) /3

a1 = float(input("ingrese valos a  "))
b1 = float(input("ingrese valos b  "))
c1 = float(input("ingrese valos c  "))
print (f"el promedio es  {promedio(a1,b1,c1)}")


print ################
