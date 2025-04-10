"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

print("Sumar los numeros comprendidos entre 0 y n")
num = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(0,num):
    suma += i

print(f"\nLa suma entre los numeros 0 y {num} es: {suma}")