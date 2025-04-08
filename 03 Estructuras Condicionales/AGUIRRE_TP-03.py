# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Ingrese su edad: "))

# if edad < 18:
#     print("Es mayor de edad!!!")
# else:
#     print("Es menor de edad!!!")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# nota = int(input("Ingrese su nota: "))

# if nota >= 6:
#     print("Aprobado!!!")
# else:
#     print("Desaprobado!!!")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar

# num = int(input("Ingrese un número PAR: "))

# if num % 2 == 0:
#     print("Ha ingresado un número PAR")
# else:
#     print("Por favor, ingrese un número PAR")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años

# edad = int(input("Ingrese su edad: "))
# if edad < 12 and edad > 0:
#     print("Usted es NIÑO")
# elif edad >= 12 and edad < 18:
#     print("Usted es ADOLESCENTE")
# elif edad >= 18 and edad < 30:
#     print("Usted es ADULTO/A JOVEN")
# elif edad > 30:
#     print("Usted es ADULTO/A MAYOR")
# else:
#     print("Ingrese una edad válida: ")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# contrasenia = str(input("Ingrese una contraseña de 8 a 14 caracteres"))

# if len(contrasenia) >= 8 and len(contrasenia) <= 14:
#     print("Ha ingresado una contraseña correcta!!!")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres!!!")

# 6) La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.

# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.

# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

# from statistics import mode, median, mean
# import random

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# media = mean(numeros_aleatorios)
# if media > mediana and mediana > moda:
#     print("Sesgo Positivo")
# elif media < mediana and mediana < moda:
#     print("Sesgo Negativo")
# elif media == mediana and mediana == moda:
#     print("Sin Sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# pal_frase = input("Ingrese una palabra o frase: ")

# if pal_frase[-1] == "a" or pal_frase[-1] == "e" or pal_frase[-1] == "i" or pal_frase[-1] == "o" or pal_frase[-1] == "u":
#     print(f"{pal_frase}!")
# else:
#     print(pal_frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre: ")
# opciones = int(input("Ingrese '1' para mayúscula, '2' para minúscula, '3' primer letra mayúscula"))
# if opciones == 1:
#     print(nombre.upper())
# elif opciones == 2:
#     print(nombre.lower())
# elif opciones == 3:
#     print(nombre.title())
# else: 
#     print("Ingrese un 1 o 2 o 3, por favor")


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

# mag_terremoto = int(input("Ingrese la magnitud del terremoto: "))
# if mag_terremoto < 3:
#     print("Muy Leve (Imperceptible)")
# elif mag_terremoto >= 3 and mag_terremoto <= 4:
#     print("Leve (ligeramente perceptible)")
# elif mag_terremoto >= 4 and mag_terremoto < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif mag_terremoto >= 5 and mag_terremoto < 6:
#     print("Fuerte (puede causar daños en estructuras débiles)")
# elif mag_terremoto >= 6 and mag_terremoto < 7:
#     print("Muy fuerte (puede causar daños significativos)")
# elif mag_terremoto >= 7:
#     print("Extremo (puede causar daños a gran escala)")
# else:
#     print("Ingrese una magnitud válida")


# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# from datetime import date

# hemisferio = input("Ingrese el hemisferio (S / N): ").strip().lower()

# while hemisferio not in ["s", "n"]:
#     print("Por favor, ingrese 'S' o 'N'.")
#     hemisferio = input("Ingrese el hemisferio (S / N): ").strip().lower()


# dia = int(input("Ingrese el día: "))
# mes = int(input("Ingrese el mes: "))
# anio = int(input("Ingrese el año: "))

# try:
#     fecha = date(anio, mes, dia)
# except ValueError as e:
#     print(f"Error al ingresar la fecha: {e}")
#     exit() # Salimos del programa si la fecha es inválida


# def determinar_estacion(fecha, hemisferio):
#     """Determina la estación del año para una fecha dada y un hemisferio."""
#     if hemisferio == "n":  # Hemisferio Norte
#         if (fecha.month == 12 and fecha.day >= 21) or (fecha.month <= 2 and fecha.day <=20):
#             return "INVIERNO"
#         elif fecha.month >= 3 and fecha.day >=21 and fecha.month <= 5 and fecha.day <=20:
#             return "PRIMAVERA"
#         elif fecha.month >= 6 and fecha.day >=21 and fecha.month <= 8 and fecha.day <=20:
#             return "VERANO"
#         else:
#             return "OTOÑO"
#     else:  # Hemisferio Sur
#         if (fecha.month == 12 and fecha.day >= 21) or (fecha.month <= 2 and fecha.day <=20):
#             return "VERANO"
#         elif fecha.month >= 3 and fecha.day >=21 and fecha.month <= 5 and fecha.day <=20:
#             return "OTOÑO"
#         elif fecha.month >= 6 and fecha.day >=21 and fecha.month <= 8 and fecha.day <=20:
#             return "INVIERNO"
#         else:
#             return "PRIMAVERA"

# estacion = determinar_estacion(fecha, hemisferio)
# print(f"Usted está en {estacion}!!!")