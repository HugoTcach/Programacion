#ALUMNA: GAMARRA JOANA

#1)

#Asignamos un valor a la variable
MAYOR_EDAD = 18
#Asignamos un valor a la variable pidiendo al usuario que ingrese un valor.
edad = int(input("Por favor ingrese su edad: "))

#Inicio del condicional If si se cumple la condición se muestra por pantalla un mensaje.
if edad >= MAYOR_EDAD:
    print("Es mayor de edad")

#2)

#Asignamos un valor a la variable pidiendo al usuario que ingrese un valor.
nota = int(input("Por favor ingrese su nota: "))

#Inicio del condicional If-else, si se cumple la condición se muestra un mensaje, si no se cumple 
#entonces se muestra otro mensaje.
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3)

#Asignamos un valor a la variable pidiendo al usuario que ingrese un número.
num = int(input("Por favor ingrese un número: "))

#Inicio del condicional If-else, si se cumple la condición se muestra un mensaje, si no se cumple
#entonces se muestra otro mensaje.
if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#4)

#Asignamos un valor a la variable pidiendo al usuario que ingrese su edad.
anios = int(input("Por favor ingrese cuántos años tiene: "))

#Inicio del condicional múltiple If-elif-else
if anios < 12:
    print("Pertenece a la categoría Niño.")
elif anios >= 12 and anios < 18:
    print("Pertenece a la categoría Adolescente.")
elif anios >= 18 and anios < 30:
    print("Pertenece a la categoría Adulto/a joven.")
else:
    print("Pertenece a la categoría Adulto/a.")

#5) 

#Asignamos un valor a la variable pidiendo al usuario que ingrese una contraseña.
clave = input("Por favor, ingrese una contraseña: ")
long = len (clave)

#Inicio el condicional If-else
if long >= 8 and long <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)

#Importamos el paquete statistics.
from  statistics import mode, median, mean

#Importamos la función random.
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Media
media = mean(numeros_aleatorios)
print(media)

#Mediana
mediana = median(numeros_aleatorios)
print(mediana)

#Moda
moda = mode(numeros_aleatorios)
print(moda)

#Inicio del condicional múltiple If-elif-else
if media > mediana and mediana > moda:
    print("Hay sesgo positivo.")
elif media < mediana  and mediana < moda:
    print("Hay sesgo negativo.")
elif media == mediana and mediana == moda and moda == media:
    print("Sin sesgo")
else:
    pass

#7)

#Pedimos al usuario que ingrese una frase o palabra.
frase_palabra = input("Por favor, ingrese una frase o palabra")

vocales = "aeiouAEIOU"

#Inicio el condicional If-else
if frase_palabra[-1] in vocales:
    frase_palabra += "!"
    print(frase_palabra)
else:
    print(frase_palabra)

#8)

#Pedimos al usuario que ingrese su nombre
nombre = input("Por favor, ingrese su nombre: ")

#Pedimos al usuario que ingrese un número del 1 al 3 
numero = int(input("Ingrese la opción que desee (1: Mayúsculas, 2: Minúsculas, 3: Primera letra mayúscula): "))

#Inicio el condicional Múltiple If-elif-else
if numero == 1:
    nombre= nombre.upper()
    print(nombre)
elif numero == 2:
    nombre = nombre.lower()
    print(nombre)
elif numero == 3:
    nombre = nombre.title()
    print(nombre)
else:
      print("La opción ingresada es invalida, por favor vuelva a intentarlo")

#9)

#Pedimos al usuario que ingrese la magnitud de un terremoto
magnitud = int(input("Por favor, ingrese la magnitud de un terremoto: "))

#Iniciamos el condicional If-elif-else
if magnitud < 3:
    print(f"Según la escala de Richter, la magnitud ingresada {magnitud} corresponde a la siguiente categoría: Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print(f"Según la escala de Richter, la magnitud ingresada {magnitud} corresponde a la siguiente categoría: Leve (ligeramente perceptible)")
elif magnitud  >= 4 and magnitud < 5:
    print(f"Según la escala de Richter, la magnitud ingresada {magnitud} corresponde a la siguiente categoría: Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print(f"Según la escala de Richter, la magnitud ingresada {magnitud} corresponde a la siguiente categoría: Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print(f"Según la escala de Richter, la magnitud ingresada {magnitud} corresponde a la siguiente categoría: Muy fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print(f"Según la escala de Richter, la magnitud ingresada {magnitud} corresponde a la siguiente categoría: Extremo (puede causar grandes daños a gran escala)")
else:
    print("El dato ingresado es invalido, por favor vuelva a intentarlo")

#10)

#Pedimos al usuario que ingrese hemisferio, mes y día
hemisferio = input("¿En qué hemisferio se encuentra?(N para norte, S para sur): ")
mes = int(input("¿Qué mes del año es? (Ingrese el mes con números): "))
dia = int(input("¿Qué día del mes es?: "))

#Iniciamos el condicional If-elif-else
if hemisferio == "N" or hemisferio == "n":
    if (mes == 12 and dia >= 21) or (mes  <= 3 and dia <= 20):
        print("Según los datos ingresados, usted se encuentra en Invierno.")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        print("Según los datos ingresados, usted se encuentra en Primavera.")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        print("Según los datos ingresados, usted se encuentra en Verano.")
    else: 
        print("Según los datos ingresados, usted se encuentra en Otoño.")
elif hemisferio == "S" or hemisferio == "s":
    if (mes == 12 and dia >= 21) or (mes  <= 3 and dia <= 20):
        print("Según los datos ingresados, usted se encuentra en Verano.")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        print("Según los datos ingresados, usted se encuentra en Otoño.")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        print("Según los datos ingresados, usted se encuentra en Invierno.")
    else: 
        print("Según los datos ingresados, usted se encuentra en Primavera.")