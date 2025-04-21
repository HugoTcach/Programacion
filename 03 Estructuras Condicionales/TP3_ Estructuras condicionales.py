# Trabajo Practico 3 - Estructuras condicionales
# Alumna: Lopez Maria Laura - Comision 16


# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga 
# “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad") 

# Nota adicional: se limitó el ejercicio a lo que se solicita, también se podría finalizar el condicional con un "else" para señalar a los 
# menores de edad. 



# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga 
# “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota_usuario = float(input("Ingrese su nota: "))
if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")



# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje 
# "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese su número: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")



# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor
#  que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. 

edad = int(input("Ingrese su edad"))
if edad < 12:
    print("Categoría: Niño/a")
elif edad >= 12 and edad < 18:
    print("Categoría: Adolescente")
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto/a joven")
elif edad >= 30:
    print("Categoría: Adulto/a")



# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una 
# contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar 
# la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("Ingrese su contraseña: ")
longitud = len(contraseña) # len muestra la cantidad de elementos
if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo
# positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. La lista contiene 50 números entre 1 y 100 elegidos de forma aleatoria.

from statistics import mode, median, mean #  el paquete statistics contiene funciones que permiten tomar una lista de números y calcular cuestiones de estadísticas
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50) ] # random.randint es una función que genera un número aleatorio y se inicia sí o sí con el import random. For i in range(50) indica un bucle que se repite 50 veces (0 a 49).
media = mean(numeros_aleatorios) # al importar statistics no es necesario desarrollar media, mediana y moda en forma manual, el paquete carga inmediatamente las funciones.
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if media > mediana > moda:
    print("El sesgo es positivo o a la derecha")
elif media < mediana < moda:
    print("El sesgo es negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se cumple ninguna de las condiciones")



# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación
# al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla.

import re # importé el módulo de expresiones regulares de python para identificar patrones
texto_usuario = input("Por favor ingrese una palabra o frase: ").strip() # usé strip para prevenir errores por si el usuario inicia o termina con un espacio.
if re.search(r'[aeiouáéíóú]$', texto_usuario, re.IGNORECASE): #r' es una raw string, evita los caracteres especiales y los saltos, $ indica que la coincidencia es en el último caracter de la palabra/cadena y re.IGNORECASE para que mayúsculas y minusculas sean indistintas.
    texto_usuario += "!" # += concatena, al ser solo el agregado de un símbolo no hace falta armar todo un print y lo que se concatena va entre comillas.
print({texto_usuario})

# Nota adicional: $ por sí solo no tiene ningún significado a menos que se importe "regex" (re). Al ser un patrón, última letra de una cadena, el $ funciona como comodín identificatorio de la posición. Si quisiera evaluarse otra que no es patrón, por ejemplo la letra del medio de una palabra, habría que recurrir a una indexación texto_usuario[posición].



# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre_usuario = input("Ingrese su nombre: ")
opcion = int(input("Elige opción 1, 2 o 3: "))
if opcion == 1:
    print(nombre_usuario.upper()) # .upper convierte el texto a mayúscula
elif opcion == 2:
    print(nombre_usuario.lower()) # .lower convierte el texto a minúscula
elif opcion == 3:
    print(nombre_usuario.title()) # .title convierte la primera letra a mayúscula



# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la 
# escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_ritcher = float(input("Ingrese la magnitud del terremoto: "))
if magnitud_ritcher < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud_ritcher < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud_ritcher < 5: 
    print("Moderado (sentido por personas pero generalmente no causa daños)")
elif 5 <= magnitud_ritcher < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud_ritcher < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud_ritcher >= 7:
    print("Extremo (puede causar graves daños a gran escala)")



# 10) Utilizando la información aportada en la tabla sobre las estaciones del año (desarrollada en el PDF del trabajo práctico) escribir un 
# programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa 
# información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio= input("Ingrese en quá hemiferio se encuentra, usando N para norte y S para sur: ")
mes = int(input("Ingrese en qué mes se encuentra, indicado con su número correspondiente (del 1 al 12): "))
dia= int(input("Ingrese el dia en que se encuentra (1 al 31): "))


if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
        print("Usted se encuentra en invierno.")
    elif (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
        print("Usted se encuentra en primavera.")
    elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
        print("Usted se encuentra en verano.")
    else:
        print("Usted se encuentra en otoño.")

if hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
        print("Usted se encuentra en verano.")
    elif (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
        print("Usted se encuentra en otoño.")
    elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
        print("Usted se encuentra en invierno.")
    else:
        print("Usted se encuentra en primavera.")

# Nota adicional: en cada hemisferio la estación faltante, colocada en el else, también podría plantearse como un elif más. 