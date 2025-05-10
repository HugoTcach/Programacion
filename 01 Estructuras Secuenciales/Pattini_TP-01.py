# Trabajo Práctico 1 Secuenciales
## Actividad 1 
print ("Hola Mundo!")

## Actividad 2
nombre = input("Escriba su nombre: ")
print (f"Buen día {nombre}!")

## Actividad 3
nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
edad = input("Escriba cuantos años tiene: ")
hogar = input("Escriba donde vive: ")
print (f"Soy {nombre} {apellido} tengo {edad} años y vivo en {hogar}")

## Actividad 4
radio = int(input("Escriba el radio de un circulo"))
area = 3.14159 * (radio**2)  ###No encontre forma de encontras a Pi como variable, tuve que utilizar una aproximación.
perimetro = (2*3.14159) * radio
print ("El área del circulo es",area,"y el perímetro es",perimetro)

## Actividad 5
print ("Escriba una cantidad de segundos")
seg = float(input())
hora = round (seg / 3600)
print (f"{seg} segundos equivalen a {hora} horas")

## Actividad 6
num = int(input("Escriba un número para desplegar su tabla de multiplicación"))
limite = int(input("Escriba el número hasta el que quiera que se multiplique"))
multiplicador = 0
while multiplicador <= limite:
    print(f"{num} * {multiplicador} = {num * multiplicador}")
    multiplicador += 1

## Actividad 7
print("Escriba dos números enteros, que no sean cero")
num1 = float(input())
num2 = float(input())
print(f"""
Resultado de {num1} + {num2} = {num1 + num2}
Resultado de {num1} / {num2} = {round(num1 / num2)}
Resultado de {num1} * {num2} = {num1 * num2}
Resultado de {num1} - {num2} = {num1 - num2}
""")

## Actividad 8
print("Escriba su altura en metros y peso en kilogramos")
altura = float(input())
peso = float(input())
imc = round (peso / (altura**2))
print(f"El índice de masa corporal es {imc}")

## Actividad 9
print ("Escriba una temperatura en grados Celsius")
celsius = int(input())
fahrenheit = ((9/5) * celsius) + 32
print (f"{celsius} grados Celsius equivalen a: {fahrenheit} grados Fahrenheit")

## Actividad 10
print ("Escriba tres números")
num1 = float(input())
num2 = float(input())
num3 = float(input())
print (f"El promedio de los tres números es: {round ((num1 + num2 + num3) / 3)}")