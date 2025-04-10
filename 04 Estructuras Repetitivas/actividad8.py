"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

print("Cuantos numeros son pares?\n")
print("Ingresa 100 numeros! Te diremos cuentos son pares\n")
pares = 0
for i in range(0, 100):
    num = int(input("Ingresa un numero entero: "))
    if num % 2 == 0:
        pares += 1

print(f"Ingresaste una cantidad de {pares} numeros pares!")