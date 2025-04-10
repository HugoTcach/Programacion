"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

print("Invertir orden de numeros!")
print("Ingrese un numero, el programa lo invertira. Ej: 547, el programa debe mostrar 745")

num = input("Ingrese un numero entero: ")
numInvertido = ""
for i in num:
    numInvertido = i + numInvertido

print(f"El numero invertido de {num} es : {numInvertido}")

