#TECNICATURA UNIVERSITARIA
#EN PROGRAMACIÓN
#A DISTANCIA
#Práctico 3: Estructuras condicionales
#Alumna Díaz Monroy Yohanna



# 1)Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


edad = int(input("Ingrese su edad: "))

if edad >= 18:
  print("Es mayor de edad")
else:
  print("Es menor de edad")


#2)Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.


nota = int(input("Ingrese su nota: "))

if nota >= 6:
  print("Aprobado")
else:
  print("Desaprobado")



#3 ejercicio 
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")



#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input("Ingrese una contraseña: ")

longitud = len(contraseña)

if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
#siguiente:
#from statistics import mode, median, mean
#mi_lista = [1,2,5,5,3]
#mean(mi_lista)
#En la documentación oficial se puede encontrar más información sobre este paquete:
#https://docs.python.org/es/3.8/library/statistics.html.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

Claro, aquí tienes el código Python que resuelve el ejercicio que planteaste:

Python

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda_numeros = mode(numeros_aleatorios)
mediana_numeros = median(numeros_aleatorios)
media_numeros = mean(numeros_aleatorios)

print(f"Moda: {moda_numeros}")
print(f"Mediana: {mediana_numeros}")
print(f"Media: {media_numeros}")

if media_numeros > mediana_numeros > moda_numeros:
    print("Sesgo positivo o a la derecha")
elif media_numeros < mediana_numeros < moda_numeros:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")






#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.


frase = input("Ingrese una frase o palabra: ")

vocales = "aeiouAEIOU"

if frase and frase[-1] in vocales:
    frase_modificada = frase + "!"
    print(frase_modificada)
else:
    print(frase)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1, 2 o 3 dependiendo de la opción que desee: "))

if opcion == 1:
    nombre_transformado = nombre.upper()
elif opcion == 2:
    nombre_transformado = nombre.lower()
elif opcion == 3:
    nombre_transformado = nombre.title()
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
    exit() #termina el programa si la opcion no es valida

print(f"Nombre transformado: {nombre_transformado}")



#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Ingrese la magnitud del terremoto en valor numerico: "))

if magnitud < 3:
    print("muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve(ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("moderado(sentido por personas , pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")    
elif magnitud < 7:
    print("Extremo (puede causar graves daños a gran escala)")  
else:
    print("richter")



#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Periodo del año
#Desde el 21 de diciembre hasta el 20 de
#marzo (incluidos)
#Desde el 21 de marzo hasta el 20 de junio
#(incluidos)
#Desde el 21 de junio hasta el 20 de
#septiembre (incluidos)
#Desde el 21 de septiembre hasta el 20 de
#diciembre (incluidos)


#Estacion en el hemisferio norte 


#invierno 
#primavera 
#verano 
#otoño 

#Estacion del año hemisferio sur 

#verano 
#otoño 
#invierno
#primavera 


#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano. 

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if hemisferio == "N":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        print("Invierno")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("Primavera")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("Verano")
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20:
        print("Otoño")
elif hemisferio == "S":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        print("Verano")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("Otoño")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("Invierno")
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20:
        print("Primavera")
else:
    print("Hemisferio no válido. Por favor, ingrese N o S.")