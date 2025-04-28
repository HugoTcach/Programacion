# 1)
edad = int(input("Ingrese su edad"))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Menor de edad")


# 2)
nota = int(input("Ingrese su nota:"))

if edad >= 6:
    print("aprobado")
else:
    print("desaprobado")
    

# 3)
num = int(input("Ingrese numero"))

if num % 2 == 0:
    print("Numero par")
else:
    print("Por favor, ingrese un numero par")
    
    
# 4)
edad = int(input("Ingrese su edad"))

if edad < 12:
    print("Es niño")
elif (edad >= 12) & (edad < 18):
    print("Es adolescente")
elif (edad >= 18) & (edad < 30):
    print("Adulto joven")
else:
    print("Es adulto")
    

# 5)
contrasenia = input("Ingrese contraseña de entre 8 a 14 caracteres")

if (len(contrasenia) >= 8) & (len(contrasenia) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    

# 6)
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

if (mode(numeros_aleatorios) < median(numeros_aleatorios)) & (median(numeros_aleatorios) < mean(numeros_aleatorios)):
    print("Sesgo positivo")
elif (mode(numeros_aleatorios) > median(numeros_aleatorios)) & (median(numeros_aleatorios) > mean(numeros_aleatorios)):
    print("Sesgo negativo")
else:
    print("No hay sesgo")
    
    
# 7)
frase = input("Ingrese una frase")
# el [-1] lo que hace es señalar al ultimo elemento de la cadena, despues el .lower()
# lo que hace es pasar a miusculas la frase y por ultimo el in 'aeiou' lo que está indicando es compare ese ultimo elemento esa cadena de caracteres que vendrian a ser las vocales
# Todo esto lo encontre en internet y quise aplicarlo
if frase[-1].lower() in 'aeiou':
    print(f'{frase}!')
else:
    print(frase)
    
    
# 8)
nombre = input("Ingrese su nombre")
option = int(input("""
                1.Si quiere sunombre en mayuscuar 
                2.Si lo desea en minusculars
                3.Si desea que la primer letra de su nombre sea en mayuscualas
                    """))

if option == 1:
    print(nombre.upper())
elif option == 2:
    print(nombre.lower())
elif option == 3:
    print(nombre.title())
else:
    print("Error")
    
    
# 9)
magnitud = float(input("Ingrese magnitud del sismo registrada"))

if (magnitud < 3):
    print("Muy leve")
elif(magnitud >= 3) & (magnitud < 4):
    print("Leve")
elif(magnitud >= 4) & (magnitud < 5):
    print("Moderada")
elif(magnitud >= 5) & (magnitud < 6):
    print("Fuerte")
elif(magnitud >= 6) & (magnitud < 7):
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")
else:
    print("No valido")
    
    
# 10)
hemisferio = input("Emisferio norte o sur? (N/S)")
mes = int(input("Mes en fomrato numerico:)"))
dia = int(input("Dia del mes"))
estacion = ""
if ((hemisferio == "S")) or (((mes == 12) & (dia >= 21)) or (mes == 1) or (mes == 2) or (mes == 3 & dia <= 20)):
    estacion = "verano"
    if hemisferio == "N":
        estacion = "invierno"
elif ((hemisferio == "S")) or (((mes == 3) & (dia >= 21)) or (mes == 4) or (mes == 5) or (mes == 6 & dia <= 20)):
    estacion = "otoño"
    if hemisferio == "N":
        estacion = "primavera"
elif ((hemisferio == "S")) or (((mes == 6) & (dia >= 21)) or (mes == 7) or (mes == 8) or (mes == 9 & dia <= 20)):
    estacion = "invierno"
    if hemisferio == "N":
        estacion = "verano"
else:
    if hemisferio == "N":
        estacion = "primavera"
    else:
        estacion = "otoño"

print(estacion)
