#incio contadores en 0
pares = 0
impares = 0
negativos = 0
positivos = 0

# Cambiar el rango de 100 a un número menor para pruebas
for _ in range(100):
    num = int(input("Ingresa un número entero: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números positivos: {positivos}")
