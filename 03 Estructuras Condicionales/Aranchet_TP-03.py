# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

# edad = int(input("Por favor, introduce tu edad: "))

# if edad >= 18:
#     print("Es mayor de edad")
# else:
#     print("Es menor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# nota = int (input("Ingresa la nota: "))
# if nota >= 6:
#     print("APROBADO")
# else:
#     print("DESAPROBADO")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero = int(input("Por favor, ingrese un número par: "))

# if numero % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Por favor, introduce tu edad: "))

# if edad < 12:
#     print("Niño/a")
# elif 12 <= edad < 18:
#     print("Adolescente")
# elif 18 <= edad < 30:
#     print("Adulto/a joven")
# else:
#     print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# contraseña = input("Ingrese una contraseña (8-14 caracteres): ")

# if 8 <= len(contraseña) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)
# import random
# from statistics import mode as moda, median as mediana, mean as media


# numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]


# moda_valor = moda(numeros_aleatorios)
# mediana_valor = mediana(numeros_aleatorios)
# media_valor = media(numeros_aleatorios)


# if media_valor > mediana_valor and media_valor > moda_valor:
#     sesgo = "sesgo positivo (cola hacia la derecha)"
# elif media_valor < mediana_valor and media_valor < moda_valor:
#     sesgo = "sesgo negativo (cola hacia la izquierda)"
# else:
#     sesgo = "no hay sesgo aparente o es simétrico"


# print(f"Lista generada: {numeros_aleatorios}")
# print(f"Moda: {moda_valor}")
# print(f"Mediana: {mediana_valor}")
# print(f"Media: {media_valor:.2f}")
# print(f"\nConclusión sobre el sesgo: {sesgo}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# frase = input("Ingrese una frase o palabra: ")

# # Verificar si la última letra es una vocal (mayúscula o minúscula)
# if len(frase) > 0 and frase[-1].lower() in ['a', 'e', 'i', 'o', 'u']:
#     frase += '!'

# print("Resultado:", frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre: ")
# opcion = input("Seleccione una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Primera letra mayúscula): ")

# if opcion == '1':
#     resultado = nombre.upper()
# elif opcion == '2':
#     resultado = nombre.lower()
# elif opcion == '3':
#     resultado = nombre.title()
# else:
#     resultado = "Opción no válida. Por favor ingrese 1, 2 o 3."

# print("Resultado:", resultado)

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

# if magnitud < 3:
#     categoria = "Muy leve (imperceptible)"
# elif 3 <= magnitud < 4:
#     categoria = "Leve (ligeramente perceptible)"
# elif 4 <= magnitud < 5:
#     categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
# elif 5 <= magnitud < 6:
#     categoria = "Fuerte (puede causar daños en estructuras débiles)"
# elif 6 <= magnitud < 7:
#     categoria = "Muy Fuerte (puede causar daños significativos)"
# else:
#     categoria = "Extremo (puede causar graves daños a gran escala)"

# print(f"Un terremoto de magnitud {magnitud} se clasifica como: {categoria}")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio te encuentras? (N para Norte / S para Sur): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

if hemisferio not in ['N', 'S'] or mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Datos ingresados no válidos.")
else:
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:  # Desde 21/9 hasta 20/12
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    if hemisferio == 'N':
        print(f"Estación actual: {estacion_norte}")
    else:
        print(f"Estación actual: {estacion_sur}")