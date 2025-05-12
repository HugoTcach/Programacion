#Ejercicio 1: "Mayoria de edad"
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Ejercicio 2: "Aprobado o Desaprobado"
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3: "Validar número par"
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4: "Clasificación por edad"
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5: "Longitud de contraseña"
contrasena = input("Ingrese una contraseña: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6: "Analizar sesgo con media, mediana y moda"
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

#Ejercicio 7: "Terminación en vocal"
frase = input("Ingrese una palabra o frase: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

#Ejercicio 8: "Transformación de nombre"
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 para MAYÚSCULAS, 2 para minúsculas, 3 para Primera Letra Mayúscula: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")

#Ejercicio 9: "Magnitud del terremoto"
magnitud = float(input("Ingrese la magnitud del terremoto según la escala de Richter: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10: "Estaciones del año"
# Pedimos los datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1 a 12): "))
dia = int(input("Ingrese el día del mes: "))

# Convertimos mes y día a un "día del año" estimado (1 a 365)
fecha = (mes * 100) + dia  # ejemplo: 21 de marzo -> 321

# Definimos la estación según el hemisferio
if hemisferio == "N":
    if 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Invierno"
elif hemisferio == "S":
    if 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Verano"
else:
    estacion = "Hemisferio no válido"

# Mostrar resultado
print(f"Estás en {estacion}.")