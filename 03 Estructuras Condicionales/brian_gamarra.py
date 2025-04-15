from statistics import mode, median, mean
import random
#exercise 1
age = int(input("Ingrese su edad: "))
if age > 18:
    print("Es mayor de edad")
#exercise 2
note = float(input("Ingrese su nota: "))
if note >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
#exercise 3
while True:
    name = int(input("Ingrese un número: "))
    if name % 2 == 0:
        print("Ha ingresado un número par")
        break
    else:
        print("Por favor, ingrese un número par")
#exercise 4
age = int(input("Ingrese su edad: "))

if age < 12:
    print("Niño/a")
elif 12 <= age < 18:
    print("Adolescente")
elif 18 <= age < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
#exercise 5
password = input("Ingrese la contraseña: ")

if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("La contraseña debe tener entre 8 y 14 caracteres")
#exercise 6
number_aleatory = [random.randint(1, 100) for _ in range(50)]
mean_value = mean(number_aleatory)
median_value = median(number_aleatory)
mode_value = mode(number_aleatory)

if mean_value == median_value == mode_value:
    result = "sin sesgo"
elif mean_value > median_value and median_value > mode_value:
    result = "sesgo positivo"
elif mean_value <median_value and median_value < mode_value:
    result = "sesgo negativo"
else:
    result = "No se puede determinar el sesgo con los criterios dados"

print(f"Mean: {mean_value:.2f}, Median: {median_value:.2f}, Mode: {mode_value}, Sesgo: {result}")
print(result)
#exercise 7
# Solicitar frase al usuario
frase = input("Ingrese una frase o palabra: ")

# Verificar si la frase termina en vocal y añadir '!' si es necesario
if len(frase) > 0:
    ultimo_caracter = frase[-1].lower()
    if ultimo_caracter in {'a', 'e', 'i', 'o', 'u'}:
        frase += '!'
print(frase)
#exercise 8
# Solicitar nombre y opción al usuario
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese la opción (1, 2, 3): ")

# Transformar el nombre según la opción
if opcion == '1':
    resultado = nombre.upper()
elif opcion == '2':
    resultado = nombre.lower()
elif opcion == '3':
    resultado = nombre.title()
else:
    resultado = nombre  # Mantener el original si la opción es inválida

# Imprimir el resultado
print(resultado)