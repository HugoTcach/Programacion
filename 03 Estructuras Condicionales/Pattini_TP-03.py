### Práctico 3: Estructuras condicionales

## Actividad 1
edad = int(input("Escriba su edad: "))
if edad >= 18: # Aún si no lo pide el ejercicio, voy a dejarlo como mayor-igual para que sea mas desarrollado.
    print("Es mayor de edad")
else:
    print("No es mayor de edad") # Voy a imprimir un mensaje si la edad sea menor a la requerida.

## Actividad 2
nota = int(input("Escriba su nota: "))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

## Actividad 3
num = int(input("Ingrese un número: "))
if num % 2 == 0: # Si bien yo personalmente usaría el condicional "while" para esta actividad, voy a dejarlo como lo pide el ejercicio.
    print("Ha ingresdo un número par")
else:
    input(print("Por favor, ingrese un número par: "))

## Actividad 4
edad = int(input("Escriba su edad: "))
if edad < 12:
    print ("Categoría Niño/a")
elif edad >= 12 and edad < 18:
    print ("Categoría Adolescente")
elif edad >= 18 and edad < 30:
    print ("Categoría Adulto/a joven")
else:
    print ("Categoría Adulto/a") # En esta línea no es necesario limitar el rango con mayor-igual 30.

## Actividad 5
contraseña = input(print("Escriba una contraseña entre 8 y 14 carácteres: "))
contraseña = len(contraseña)
if contraseña >= 8 and contraseña <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    input(print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")) # En esta parte también se puede utilizar el condicional "while".

## Actividad 6
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
from statistics import mode, median , mean 
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if (media > mediana) and (mediana > moda):
    print("Hay Sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print("Hay Sesgo negativo")
elif (media == mediana) and (mediana == moda): # En la actividad aclara que solo en el caso de que las tres variables sean iguales equivale a "No hay sesgo". Por eso lo indico de esta forma.
    print("No hay Sesgo")
else:
    print("No se puede determinar")

## Actividad 7
palabra = input(print("Escriba una frase, o una palabra: "))
letra = str(palabra[-1]); letra = letra.upper()               # En esta linea voy a transformar el cáracter ingresado y transformarlo para unificar las vocales a mayúsculas.
if (letra == "A") or (letra == "E") or (letra == "I") or (letra == "O") or (letra == "U"):
    print(f"{palabra}" + "!")
else:
    print(f"{palabra}")

## Actividad 8
[print("""
Escriba su nombre y elija una opción de las siguientes:
Opción 1: Si quiere su nombre en mayúsculas.
Opción 2: Si quiere su nombre en minúsculas.
Opción 3: Si quiere su nombre con la primera letra mayúscula.""")]
nombre = input("")
opcion = int(input())
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("No ha ingresado una opción valida.")

## Actividad 9
magnitud = int(input(print("Ingrese la magnitud del terremoto: ")))
if (magnitud >= 1) and (magnitud < 3): # Agrego una condición adicional, siendo que logicamente no puede haber magnitud negativa.
    print("Muy leve; imperceptible.")
elif (magnitud >= 3) and (magnitud < 4):
    print("Leve; ligeramente perceptible.")
elif (magnitud >= 4) and (magnitud < 5):
    print("Moderado; sentido por personas, pero generalmente no causa daños.")
elif (magnitud >= 5) and (magnitud < 6):
    print("Fuerte; puede causar daños en estructuras débiles.")
elif (magnitud >= 6) and (magnitud < 7):
    print("Muy Fuerte; puede causar daños significativos.")
elif magnitud >= 7:
    print("Extremo; puede causar graves daños a gran escala.")
elif magnitud == 0:
    print("No hubo actividad sísmica.")
else:
    print(f"{magnitud} no es una magnitud válida.")

## Actividad 10
[print("""
Indique en qué hemisferio se encuentra, Norte (N) o Sur (S):
Ingrese el nombre del mes y la fecha del día.""")]
hemisferio = input(print("")); hemisferio = hemisferio.upper()
mes = input(print("")); mes = mes.lower()
dia = int(input(print()))
if hemisferio == "S":   # Al haber solo dos hemisferios, solo basta con aclarar uno de ellos.
    if (mes == "diciembre" and (dia >= 21)) or (mes == "enero") or (mes == "febrero") or ((mes == "marzo") and (dia <= 20)):
        print("Se encuentar en la estación Verano.")
    elif (mes == "marzo" and (dia >= 21)) or (mes == "abril") or (mes == "mayo") or ((mes == "junio") and (dia <= 20)):
        print("Se encuentar en la estación Otoño.")
    elif (mes == "junio" and (dia >= 21)) or (mes == "julio") or (mes == "agosto") or ((mes == "septiembre") and (dia <= 20)):
        print("Se encuentar en la estación Invierno.")
    elif (mes == "septiembre" and (dia >= 21)) or (mes == "octubre") or (mes == "noviembre") or ((mes == "diciembre") and (dia <= 20)):
        print("Se encuentar en la estación Primavera.")
    else:
        print("No ha ingresado un mes válido")
if hemisferio == "N":
    if (mes == "diciembre" and (dia >= 21)) or (mes == "enero") or (mes == "febrero") or ((mes == "marzo") and (dia <= 20)):
        print("Se encuentar en la estación Invierno.")
    elif (mes == "marzo" and (dia >= 21)) or (mes == "abril") or (mes == "mayo") or ((mes == "junio") and (dia <= 20)):
        print("Se encuentar en la estación Primavera.")
    elif (mes == "junio" and (dia >= 21)) or (mes == "julio") or (mes == "agosto") or ((mes == "septiembre") and (dia <= 20)):
        print("Se encuentar en la estación Verano.")
    elif (mes == "septiembre" and (dia >= 21)) or (mes == "octubre") or (mes == "noviembre") or ((mes == "diciembre") and (dia <= 20)):
        print("Se encuentar en la estación Otoño.")
    else:
        print("No ha ingresado un mes válido")
if (hemisferio != "S") and (hemisferio != "N"):
    print("No ha ingresado un hemisferio válido.") # En esta actividad, si bien no existen meses con días 0 o negativos, o con más de 31, solo es necesario condicionarlo en aquellos meses con equinoccios y solsticios.