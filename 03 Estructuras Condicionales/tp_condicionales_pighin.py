#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad"


# Paso 1: Solicitar al usuario que ingrese su edad
# Usamos la función input() para pedir el dato, y lo convertimos a entero con int()
edad = int(input("ingrese su edad: "))

# Paso 2: Verificar si la edad es mayor o igual a 18
# Si la condición se cumple (edad >= 18), mostramos el mensaje correspondiente
if edad >= 18 :
    print("es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el


# Paso 1: Solicitar al usuario que ingrese su nota
# Usamos input() para pedir el valor y lo convertimos a entero con int()

nota = int(input("ingrese su nota : "))
# Paso 2: Evaluar si la nota es mayor o igual a 6
# Si es así, el alumno está aprobado
if nota >= 6 :
    print("Aprobado")

# Paso 3: Si la condición no se cumple (nota menor a 6), está desaprobado
else:
    print("Desaprobado")



#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 

# Paso 1: Solicitar al usuario que ingrese un número
# Usamos input() para pedir el dato y lo convertimos a entero con int()
numero = int(input("Ingrese un numero : "))

# Paso 2: Verificar si el número es par
# Usamos el operador módulo (%) para obtener el resto de la división por 2
# Si el resto es igual a 0, significa que el número es par
if numero % 2 ==0 :
    print("Ha ingresado un numero par")

# Paso 3: Si el número no es par (es impar), mostramos el mensaje de error
else: 
    print("Por favor ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

# Paso 1: Pedir al usuario que ingrese su edad
# Usamos input() para solicitar el dato y lo convertimos a entero con int()

edad = int(input("Ingrese su edad : "))

# Paso 2: Evaluar a qué categoría pertenece según la edad
if edad < 12 :
     # Paso 2: Evaluar a qué categoría pertenece según la edad
     print("Niño/a")

elif edad >= 12 and edad < 18 :
     # Si la edad es entre 12 y 17, es Adolescente
    print("Adolescente")
elif edad >= 18 and edad < 30 :
     # Si la edad es entre 18 y 29, es Adulto/a joven
    print ("Adulto/a")
else: 

 # Si la edad es 30 o más, es Adulto/a
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string


# Paso 1: Pedimos al usuario que ingrese una contraseña
contraseña = input("Ingrese su contraseña: ")

# Paso 2: Mientras la contraseña NO tenga entre 8 y 14 caracteres, seguimos pidiéndola
# Usamos len() para contar la cantidad de caracteres del string
# La condición es: si la longitud es menor a 8 o mayor a 14, la contraseña no es válida

while len(contraseña) < 8 or len(contraseña) > 14:
    # Si la contraseña es inválida, mostramos un mensaje de error
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    # Volvemos a pedir la contraseña hasta que cumpla con la condición
    contraseña = input("Ingrese su contraseña: ")

# Paso 3: Cuando la contraseña tiene una longitud correcta, salimos del bucle
# Mostramos el mensaje de confirmación
print("Ha ingresado una contraseña correcta")



# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Importamos las librerías necesarias

import random 
from statistics import mode, median, mean 

# Creamos una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Mostramos los valores obtenidos
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Determinamos el tipo de sesgo comparando media, mediana y moda

if media > mediana and mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana and mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

#7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Pedimos al usuario una frase o palabra
texto = input("escriba una palabra o frase : ")
# Obtenemos el último carácter del texto
ultimo_caracter = texto [-1]

# Verificamos si el último carácter es una vocal
if ultimo_caracter.lower () in "aeiou" :
  # Si termina en vocal, le agregamos un signo de exclamación

    texto = texto + "!"

# Imprimimos el resultado
print (texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:


# Pedimos el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Pedimos la opción deseada
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para primera letra mayúscula: ")

# Transformamos el nombre según la opción elegida
if opcion == "1":
    nombre = nombre.upper()
elif opcion == "2":
    nombre = nombre.lower()
elif opcion == "3":
    nombre = nombre.title()
else:
    print("Opción no válida")

# Mostramos el resultado
print(nombre)


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla.


# Pedimos la magnitud del terremoto al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasificamos según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")



#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.


# Pedir datos al usuario
hemisferio = input("Ingrese el hemisferio (N para Norte, S para Sur): ")
mes = int(input("Ingrese el mes (en número, por ejemplo 1 para enero, 12 para diciembre): "))
dia = int(input("Ingrese el día del mes: "))

# Determinar estación según mes y día
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    print("Fecha no válida.")
    estacion_norte = estacion_sur = None

# Mostrar la estación
if estacion_norte and estacion_sur:
    if hemisferio.upper() == "N":
        print(f"Estás en {estacion_norte}")
    elif hemisferio.upper() == "S":
        print(f"Estás en {estacion_sur}")
    else:
        print("Hemisferio no válido.")



