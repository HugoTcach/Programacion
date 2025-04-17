# Ejercicio 1

def imprimir_hola_mundo():
    return "Hola Mundo!"

print(imprimir_hola_mundo())


# Ejercicio 2

def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

saludar_usuario("Belen")

# Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}.")

print("Ingrese sus datos:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia:")

informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4

def calcular_area_circulo(radio):
    return 3.14 * (radio * radio)

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = float(input("Ingresa el radio de un circulo: "))

print(f"El area de un circulo es {calcular_area_circulo(radio)}")

print(f"El perimetro de un circulo es {calcular_perimetro_circulo(radio)}")

# Ejercicio 5

def segundos_a_horas(segundos):
    return segundos // 3600

segundos = int(input("Ingrese la cantidad de segundos: "))

print(f"La cantidad de horas son {segundos_a_horas(segundos)}.")

# Ejercicio 6

def tabla_multiplicar(numero):
    for cont in range(0,10):
        cont += 1
        resultado = numero * cont
        print(f"{numero} x {cont} = {resultado}")

numero = int(input("Ingrese un numero: "))

tabla_multiplicar(numero)

# Ejercicio 7

def operaciones_basicas(a,b):
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicacion: {a * b}")
    print(f"Division: {a / b}")

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese un numero: "))

operaciones_basicas(num_1, num_2)

# Ejercicio 8

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

peso = float(input("Ingrese su peso: "))

altura = float(input("Ingrese su altura: "))

print(f"Tu IMC es de {calcular_imc(peso, altura):.2f}")

# Ejericio 9

def celsius_a_fahrenheit(celsius):
    F = celsius = (celsius * (9/5)) + 32
    return F

temperatura = float(input("Ingresa grados C°: "))

print(f"La temperatura es de {celsius_a_fahrenheit(temperatura)}° Fahrenheit.")

# Ejercicio 10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num_1 = int(input("Primer numero: "))
num_2 = int(input("Segundo numero: "))
num_3 = int(input("Tercer numero: "))
prom = calcular_promedio(num_1, num_2, num_3)

print(f"El promedio de todos los numeros es de {prom}")
