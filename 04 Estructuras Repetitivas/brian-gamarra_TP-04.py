import random
#exercise 1
for numero in range(101):
    print(numero)
#exercise 2
number = abs(int(input("Ingrese un número entero: ")))
number_digits = len(str(number)) if number != 0 else 1
print(f"El número ingresado tiene {number_digits} dígitos")
#exercise 3
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
menor = min(num1, num2)
mayor = max(num1, num2)
inicio = menor + 1
fin = mayor - 1

suma = sum(range(inicio, fin + 1)) if inicio <= fin else 0

print(f"La suma de los números entre {num1} y {num2} (excluyéndolos) es: {suma}")
#exercise 4
total = 0

while True:
    entrada = input("Ingrese un número entero (0 para finalizar): ").strip()
    if entrada == "0":
        break
    try:
        numero = int(entrada)
        total += numero
    except ValueError:
        print("⚠️ Entrada inválida. Ingrese solo números enteros.")

print(f"\nTotal acumulado: {total}")
#exercise 5
numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    try:
        entrada = input("Adivina el número (0-9): ")
        numero_usuario = int(entrada)
        
        if numero_usuario < 0 or numero_usuario > 9:
            print("⚠️ El número debe estar entre 0 y 9.")
            continue  # No cuenta como intento válido
        
        intentos += 1
        
        if numero_usuario == numero_secreto:
            print(f"¡Correcto! El número era {numero_secreto}.")
            break
        else:
            print("Incorrecto. Sigue intentando.")
            
    except ValueError:
        print("⚠️ Ingresa solo números enteros.")

print(f"Total de intentos: {intentos}")
#exercise 6
for numero in range(100, -1, -2):
    print(numero)
#exercise 7
try:
    number = int(input("ingrese el numero entero positivo: "))
    if number < 0:
        print("⚠️ Error: el numero debe ser positivo.")
    else:
        total = sum(range(number + 1))  # Sum from 0 to 'number' (inclusive)
        print(f"la suma de todos los numeros entre 0 y {number} es: {total}")
except ValueError:
    print("⚠️ Error: ingrese un numero entero valido.")
#exercise 8
CANTIDAD_NUMEROS = 100  # Cambiar este valor para pruebas (ejemplo: 5)

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {CANTIDAD_NUMEROS} números enteros:")

for i in range(CANTIDAD_NUMEROS):
    while True:
        entrada = input(f"Número {i + 1}: ").strip()
        try:
            numero = int(entrada)
            break
        except ValueError:
            print("⚠️ Error: Ingrese un número entero válido.")
    
    # Contar pares/impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contar positivos/negativos (el 0 no se cuenta)
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"- Pares: {pares}")
print(f"- Impares: {impares}")
print(f"- Positivos: {positivos}")
print(f"- Negativos: {negativos}")
#exercise 9
CANTIDAD_NUMEROS = 100  # Cambiar este valor para pruebas (ej: 5)

suma = 0

print(f"Ingrese {CANTIDAD_NUMEROS} números enteros:")

for i in range(CANTIDAD_NUMEROS):
    while True:
        entrada = input(f"Número {i + 1}: ").strip()
        try:
            numero = int(entrada)
            suma += numero
            break
        except ValueError:
            print("Error: Ingrese un número entero válido.")

media = suma / CANTIDAD_NUMEROS
print(f"\nLa media de los {CANTIDAD_NUMEROS} números es: {media:.2f}")
#exercise 10
try:
    numero = int(input("Ingrese un número entero: "))
    numero_abs = abs(numero)
    invertido = int(str(numero_abs)[::-1])
    resultado = -invertido if numero < 0 else invertido
    print(f"Número invertido: {resultado}")
except ValueError:
    print("Error: Ingrese un número entero válido.")