#1) 

#Se muestra un mensaje a usuario contandole lo que va a ver en este programa.
print("A contunación le mostraremos todos los números enteros desde el 0 hasta el 100.")

#Se define la variable cont.
cont = 0

#Se crea un bucle for.
for cont in range (0, 100+1):
    print(cont)
    cont += cont

#2)

#Se define la variable num a través de un input, pidiendo al usuario que ingrese un número entero.
num = input("Por favor ingrese un número entero: ")

#Se da uso a la función len().
longitud = len(num)

#Se le muestra al usuario la cantidad de dígitos que tiene el número que ingresó.
print(f"La cantidad de dígitos que contiene el número que ingresaste {num} es de {longitud}.")

#3)

#Se le muestra al usuario un mensaje explicandole los datos que debe ingresar.
print("A continuación deberá ingresar dos números enteros para que luego el programa le muestre el" \
" resultado de la suma de todos los númros comprendidos entre los dos números ingresados.")

#Se definen las variables num1 y num2.
num1 = int(input("Por favor ingrese el primer número entero: "))
num2 = int(input("Por favor ingrese el segundo número entero: "))

#Se definen las variables suma y contad.
suma = 0
contad = 1

#Se da inicio a un bucle For.
for contad in range (num1+1, num2):
    suma = suma + contad
    
#Se muestra el resultado de la suma al usuario. 
print(f"El resultado de la suma de los números comprendidos entre {num1} y {num2} es de {suma}.")

#4)

#Se muestra un mensaje al usuario con los pasos a seguir.
print("A continuación deberá ingresar números enteros " \
"que serán sumados de forma secuencial, cuando quiera ver el resultado, " \
"ingrese el número 0.")

#Se definen las variables numero, contador y resultado.
numero = 1
contador = 0
resultado = 0

while numero != 0:
    #Se le pide al usuario que ingrese un número entero y es asignado a la variable numero.
    numero = int(input("Ingrese un número entero: "))
    resultado += numero
print(f"El resultado de la suma de los números ingresados es {resultado}.")

#5)

#Se importa el módulo  random.
import random

num_aleatorio = random.randint(0, 9) #Generá un número aleatorio entre el 0 y 9 incluidos.

#Se le da la bienvenida al jugador.
print("Bienvenido! En este juego se pondrán a prueba sus habilidades para las adivinanzas.")

#Intrucciones para el jugador y se define la variable num_jugador.
num_jugador = int(input("A continuación deberá adivinar un número aleatorio entres 0 y 9: "))

intentos = 1

#Se inicia el bucle while.
while num_aleatorio != num_jugador:
    num_jugador = int(input("INCORRECTO. Por favor vuelva a intentarlo, recuerde que debe ser un número entre 0 y 9:  "))
    intentos += 1

#Si el jugador adivina el número se le muestran estos mensajes.
print("CORRECTO! Felicidades, has logrado superar esta prueba.")
print(f"Para lograr adivinar el número debiste hacer {intentos} intentos.")

#6) 

#Se muestra un mensaje a usuario contandole lo que va a ver en este programa.
print("A contunación le mostraremos todos los números pares comprendidos entre  0 y 100 de forma decreciente.")

#Se define la variable cont.
cont = 0

#Se crea un bucle for.
for cont in range (100-2, 0, -2):
    print(cont)
    cont -= cont

#7)

#Se le muestra al usuario un mensaje explicandole los datos que debe ingresar.
print("A continuación deberá ingresar un número entero para que luego el programa le muestre el" \
" resultado de la suma de todos los númros comprendidos entre el 0 y el número ingresado.")

#Se define la variable num1.
num1 = int(input("Por favor ingrese un número entero: "))


#Se definen las variables suma_a y contad_a.
suma_a = 0
contad_a = 1

#Se da inicio a un bucle For.
for contad_a in range (0, num1):
    suma_a = suma_a + contad_a
    
#Se muestra el resultado de la suma al usuario. 
print(f"El resultado de la suma de los números comprendidos entre 0 y {num1} es de {suma_a}.")

#8)

#Se declaran las variables.
par = 0
impar = 0
positivo = 0
negativo = 0

#Se inicia una estructura repetitiva For.
for _ in range(100):  # Repetir 100 veces
    num_entero = 0
    while num_entero == 0:    #Dentro del bucle for anidamos un bucle while.
        num_entero = int(input("Ingrese un número entero distinto de cero: "))   #Mensaje para el usuario.
        if num_entero == 0:   #Estructura condicional if.
            print("Error. El dato ingresado es incorrecto. Por favor vuelva a intentarlo.")
    #Estructuras condiconales.
    if num_entero > 0:
        positivo += 1
    else:
        negativo += 1

    if num_entero % 2 == 0:
        par += 1
    else:
        impar += 1

#Mensaje final mostrando los números pares, impares, positivos y negativos.
print("\nCon los números ingresados se crearon cuatro grupos: pares, impares, positivos y negativos.")
print(f"Hemos analizado y separado por grupos cada número ingresado. Ha ingresado {par} números pares, {impar} números impares, {positivo} números positivos y {negativo} números negativos.")

#9)

#Cantidad de número que se pueden ingresar.
cantidad = 100

#Se define suma_num y el contador "c".
suma_num = 0
c = 0  

#Estructura repetitiva while.
while c < cantidad:
    entrada = input(f"Ingrese el número entero #{c + 1}: ") #Se pide un número.

    #Para evitar errores si el usuario ingresa otro valor, 
    # se da uso a la estructura de control de errores try/except.
    try:
        numero = float(entrada)
        if not numero.is_integer():
            print("Error: Ingrese un número entero, no decimal.")
            continue
        num_entero = int(numero)
        suma_num += num_entero
        c += 1
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

#Como paso final se calcula la media y se muestra el resultado por pantalla.
media = suma_num / cantidad
print(f"\nLa media de los {cantidad} números ingresados es {media}.")

#10)

# Se le pide al usuario que ingrese un número.
print("A continuación deberá ingresar un número. Luego le mostraremos ese mismo número pero de forma invertida.")

# Inicializamos la variable para que entre al bucle
numero = input("Por favor, ingrese un número: ")

# Mientras el número no sea un entero válido, pedir un número válido.
while not numero.lstrip("-").isdigit():
    print("Error: Ingrese un número entero válido.")
    numero = input("Por favor, ingrese un número: ")

# Se invierte el número una vez validado con el método de cadenas .lstrip() y .isdigit()
numero_invertido = numero[::-1] if numero[0] != "-" else "-" + numero[:0:-1]
print("Número invertido:", numero_invertido)