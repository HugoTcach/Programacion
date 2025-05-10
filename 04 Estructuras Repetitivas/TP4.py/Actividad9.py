suma = 0

# Cambiar el rango de 100 a un número menor para pruebas
for _ in range(100):
    num = int(input("Ingresa un número entero: "))
    suma += num

media = suma / 100
print(f"La media de los números ingresados es: {media}")
